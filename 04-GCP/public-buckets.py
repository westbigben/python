import os
import sys
from google.cloud import storage

def check_for_public_buckets(project_id: str):
    """
    Checks all buckets in a project for public access and reports findings.

    Args:
        project_id: The ID of the GCP project to audit.
    """
    
    # These are the members that grant public access
    public_members = ["allUsers", "allAuthenticatedUsers"]
    
    try:
        # Initialize the storage client for the specified project
        client = storage.Client(project=project_id)
        
        # List all buckets in the project
        buckets = client.list_buckets()
        
        print(f"Auditing Cloud Storage buckets for project: {project_id}\n")
        
        public_buckets = []
        for bucket in buckets:
            # Get the IAM policy for the current bucket
            policy = bucket.get_iam_policy(requested_policy_version=3)
            
            # Iterate through each role binding in the policy
            for binding in policy.bindings:
                # Check if any public member is present
                if any(member in binding["members"] for member in public_members):
                    print(f"🚨 WARNING: Bucket '{bucket.name}' is publicly accessible via the role '{binding['role']}'.")
                    public_buckets.append(bucket.name)
                    # We can break from this inner loop once a violation is found for a bucket
                    break
        
        print("\n" + "="*50)
        if public_buckets:
            print("Summary: The following buckets have public access permissions:")
            for bucket_name in public_buckets:
                print(f"- {bucket_name}")
        else:
            print("✅ All buckets checked are secure and do not have public access.")
            
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # Get the project ID from an environment variable
    project_id = os.environ.get("GCP_PROJECT_ID")

    if not project_id:
        print("Error: The GCP_PROJECT_ID environment variable must be set.")
        sys.exit(1)
        
    check_for_public_buckets(project_id)