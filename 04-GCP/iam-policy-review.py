import os
import sys
from google.cloud import resourcemanager_v3

def review_broad_iam_roles(project_id: str):
    """
    Reviews the IAM policies for a given project to identify members with broad roles.

    Args:
        project_id: The ID of the GCP project to audit.
    """
    
    broad_roles = ["roles/owner", "roles/editor"]
    
    try:
        client = resourcemanager_v3.ProjectsClient()
        
        # Get the project's IAM policy
        policy = client.get_iam_policy(resource=f"projects/{project_id}")
        
        found_violations = False
        print(f"Auditing IAM policy for project: {project_id}\n")
        
        # Iterate through each binding in the policy
        for binding in policy.bindings:
            role = binding.role
            
            # Check if the role is a broad role
            if role in broad_roles:
                found_violations = True
                print(f"🚨 Found broad role '{role}' assigned to the following members:")
                for member in binding.members:
                    print(f"- {member}")
                print("-" * 50)
        
        if not found_violations:
            print("✅ No broad roles were found in the project's IAM policy.")
            
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # Get the project ID from an environment variable
    project_id = os.environ.get("GCP_PROJECT_ID")

    if not project_id:
        print("Error: The GCP_PROJECT_ID environment variable must be set.")
        sys.exit(1)
        
    review_broad_iam_roles(project_id)