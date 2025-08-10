import os
import sys
from google.cloud import compute_v1

def delete_unused_ip_addresses(project_id: str, region: str):
    """
    Finds and deletes unattached static IP addresses in a specified project and region.
    
    Args:
        project_id: The ID of the GCP project.
        region: The GCP region to check for IP addresses.
    """
    
    try:
        addresses_client = compute_v1.AddressesClient()
        
        # List all IP addresses in the target project and region
        request = compute_v1.ListAddressesRequest(project=project_id, region=region)
        addresses_list = addresses_client.list(request=request)
        
        # Check for unattached IP addresses
        for address in addresses_list.items:
            # A static IP is unused if its 'status' is 'RESERVED'
            if address.status == "RESERVED":
                print(f"Found unused IP address: {address.name} ({address.address}). Deleting...")
                
                # Create a delete request
                delete_request = compute_v1.DeleteAddressRequest(
                    project=project_id,
                    region=region,
                    address=address.name,
                )
                
                # Execute the delete operation
                operation = addresses_client.delete(request=delete_request)
                
                # Wait for the operation to complete
                wait_for_extended_operation(operation, addresses_client)
                
                print(f"IP address '{address.name}' successfully deleted.")
            else:
                print(f"IP address '{address.name}' ({address.status}) is in use. Skipping.")
                
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        
def wait_for_extended_operation(operation, client):
    """Waits for an extended operation to complete."""
    while operation.status != "DONE":
        # Refresh the operation status
        operation = client.get_region_operation(
            project=operation.target_link.split('/')[6],
            region=operation.target_link.split('/')[8],
            operation=operation.name,
        )
    if operation.error:
        raise Exception(f"Operation failed with error: {operation.error}")

if __name__ == "__main__":
    # Get variables from environment
    project_id = os.environ.get("GCP_PROJECT_ID")
    region = os.environ.get("GCP_REGION")

    if not project_id or not region:
        print("Error: GCP_PROJECT_ID and GCP_REGION environment variables must be set.")
        sys.exit(1)
    
    print(f"Starting IP address cleanup for project '{project_id}' in region '{region}'...")
    delete_unused_ip_addresses(project_id, region)