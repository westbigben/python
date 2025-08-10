import os
import sys
from google.cloud import compute_v1

def stop_labeled_vms(request):
    """
    Stops all VM instances with a specific label in a given project and zone.
    This function is designed to be triggered by Cloud Scheduler.

    Args:
        request: A Flask request object. The body is not used, but the function
                 is triggered by an HTTP call from Cloud Scheduler.
    """
    
    # Get configuration from environment variables
    project_id = os.environ.get("GCP_PROJECT_ID")
    zone = os.environ.get("GCP_ZONE")
    label_key = os.environ.get("VM_LABEL_KEY")
    label_value = os.environ.get("VM_LABEL_VALUE")

    if not all([project_id, zone, label_key, label_value]):
        print("Error: Required environment variables not set.")
        sys.exit(1)
    
    print(f"Stopping VMs in project '{project_id}', zone '{zone}' with label '{label_key}={label_value}'...")
    
    try:
        instances_client = compute_v1.InstancesClient()
        
        # Build the filter for the list request
        filter_str = f'labels.{label_key}="{label_value}"'
        
        request = compute_v1.ListInstancesRequest(
            project=project_id,
            zone=zone,
            filter=filter_str
        )
        
        # List all instances that match the filter
        instances_list = instances_client.list(request=request)
        
        for instance in instances_list.items:
            # Only stop running instances
            if instance.status == "RUNNING":
                print(f"Stopping VM: {instance.name}...")
                stop_request = compute_v1.StopInstanceRequest(
                    project=project_id,
                    zone=zone,
                    instance=instance.name,
                )
                operation = instances_client.stop(request=stop_request)
                
                # Wait for the operation to complete
                wait_for_extended_operation(operation, instances_client)
                
                print(f"VM '{instance.name}' stopped successfully.")
            else:
                print(f"VM '{instance.name}' is already '{instance.status}'. Skipping.")

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

def wait_for_extended_operation(operation, client):
    """Waits for an extended operation to complete."""
    while operation.status != "DONE":
        operation = client.get_zone_operation(
            project=operation.target_link.split('/')[6],
            zone=operation.target_link.split('/')[8],
            operation=operation.name,
        )
    if operation.error:
        raise Exception(f"Operation failed with error: {operation.error}")