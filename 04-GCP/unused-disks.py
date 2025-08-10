import os
import sys
from google.cloud import compute_v1

def delete_unused_disks(project_id: str, zone: str):
    """
    Finds and deletes unattached disks in a specified project and zone.
    
    Args:
        project_id: The ID of the GCP project.
        zone: The GCP zone to check for disks.
    """
    
    try:
        # Initialize the Compute Engine client for the specified zone
        disks_client = compute_v1.DisksClient()
        
        # List all disks in the target project and zone
        request = compute_v1.ListDisksRequest(project=project_id, zone=zone)
        disks_list = disks_client.list(request=request)
        
        # Check for unattached disks
        for disk in disks_list.items:
            # A disk is unattached if the 'users' list is empty
            if not disk.users:
                print(f"Found unattached disk: {disk.name}. Attempting to delete...")
                
                # Create a delete request
                delete_request = compute_v1.DeleteDiskRequest(
                    project=project_id,
                    zone=zone,
                    disk=disk.name,
                )
                
                # Execute the delete operation and wait for it to complete
                operation = disks_client.delete(request=delete_request)
                
                # Optional: You can implement a function to wait for the operation
                # to ensure it completes before the script finishes.
                wait_for_extended_operation(operation, disks_client)
                
                print(f"Disk '{disk.name}' successfully deleted.")
            else:
                print(f"Disk '{disk.name}' is in use by: {disk.users}. Skipping.")
                
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        
def wait_for_extended_operation(operation, client):
    """Waits for an extended operation to complete."""
    while operation.status != "DONE":
        # Refresh the operation status
        operation = client.get_zone_operation(
            project=operation.target_link.split('/')[6],
            zone=operation.target_link.split('/')[8],
            operation=operation.name,
        )
    if operation.error:
        raise Exception(f"Operation failed with error: {operation.error}")

if __name__ == "__main__":
    # Get variables from environment
    project_id = os.environ.get("GCP_PROJECT_ID")
    zone = os.environ.get("GCP_ZONE")

    if not project_id or not zone:
        print("Error: GCP_PROJECT_ID and GCP_ZONE environment variables must be set.")
        sys.exit(1)
    
    print(f"Starting disk cleanup for project '{project_id}' in zone '{zone}'...")
    delete_unused_disks(project_id, zone)
