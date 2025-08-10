# GCP Management Scripts

This repository contains Python scripts for managing Google Cloud Platform resources, including VM management, disk cleanup, IP address management, security auditing, and IAM policy review.

## 📋 Prerequisites

1. **Python 3.7+** installed on your system
2. **Google Cloud SDK** configured with appropriate permissions
3. **Service Account** with necessary IAM roles for the resources you want to manage
4. **Authentication** set up (either via service account key or gcloud auth)

## 🚀 Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd 04-GCP
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 📚 Scripts Overview

### 1. **unused-disks.py** - Disk Cleanup Script
**Purpose**: Finds and deletes unattached disks in a specified GCP project and zone.

**Environment Variables Required**:
- `GCP_PROJECT_ID`: Your Google Cloud Project ID
- `GCP_ZONE`: The GCP zone to check for disks (e.g., `us-central1-a`, `europe-west1-b`)

**Usage**:
```bash
export GCP_PROJECT_ID="your-project-id"
export GCP_ZONE="us-central1-a"
python unused-disks.py
```

**⚠️ Warning**: This script will permanently delete unattached disks. Use with caution!

---

### 2. **shutdown-vms.py** - VM Shutdown Script
**Purpose**: Stops all VM instances with a specific label in a given project and zone. Designed to be triggered by Cloud Scheduler.

**Environment Variables Required**:
- `GCP_PROJECT_ID`: Your Google Cloud Project ID
- `GCP_ZONE`: The GCP zone where VMs are located
- `VM_LABEL_KEY`: The label key to filter VMs (e.g., `environment`)
- `VM_LABEL_VALUE`: The label value to match (e.g., `dev`, `staging`)

**Usage**:
```bash
export GCP_PROJECT_ID="your-project-id"
export GCP_ZONE="us-central1-a"
export VM_LABEL_KEY="environment"
export VM_LABEL_VALUE="dev"
python shutdown-vms.py
```

---

### 3. **delete-unused-ips.py** - IP Address Cleanup Script
**Purpose**: Finds and deletes unattached static IP addresses in a specified project and region.

**Environment Variables Required**:
- `GCP_PROJECT_ID`: Your Google Cloud Project ID
- `GCP_REGION`: The GCP region to check for IP addresses (e.g., `us-central1`, `europe-west1`)

**Usage**:
```bash
export GCP_PROJECT_ID="your-project-id"
export GCP_REGION="us-central1"
python delete-unused-ips.py
```

**⚠️ Warning**: This script will permanently delete unused static IP addresses. Use with caution!

---

### 4. **public-buckets.py** - Security Audit Script
**Purpose**: Checks all Cloud Storage buckets in a project for public access and reports security findings.

**Environment Variables Required**:
- `GCP_PROJECT_ID`: Your Google Cloud Project ID

**Usage**:
```bash
export GCP_PROJECT_ID="your-project-id"
python public-buckets.py
```

**🔒 Security**: This script only reports findings and does not make any changes to your buckets.

---

### 5. **iam-policy-review.py** - IAM Policy Audit Script
**Purpose**: Reviews the IAM policies for a given project to identify members with broad roles (owner, editor).

**Environment Variables Required**:
- `GCP_PROJECT_ID`: Your Google Cloud Project ID

**Usage**:
```bash
export GCP_PROJECT_ID="your-project-id"
python iam-policy-review.py
```

**🔒 Security**: This script only reports findings and does not make any changes to your IAM policies.

---

## 🔐 Required IAM Roles

To use these scripts, your service account or user account needs the following roles:

### For Compute Engine Scripts (unused-disks.py, shutdown-vms.py):
- `roles/compute.instanceAdmin.v1` - For VM management
- `roles/compute.storageAdmin` - For disk management

### For Network Scripts (delete-unused-ips.py):
- `roles/compute.networkAdmin` - For IP address management

### For Storage Scripts (public-buckets.py):
- `roles/storage.admin` - For bucket IAM policy access

### For IAM Scripts (iam-policy-review.py):
- `roles/resourcemanager.projectIamAdmin` - For project IAM policy access

## 🛡️ Security Best Practices

1. **Use Service Accounts**: Create dedicated service accounts with minimal required permissions
2. **Enable Audit Logging**: Monitor all actions performed by these scripts
3. **Test in Non-Production**: Always test scripts in development/staging environments first
4. **Review Changes**: Regularly review what resources are being modified or deleted
5. **Backup Critical Data**: Ensure important data is backed up before running cleanup scripts

## 🚨 Important Notes

- **Destructive Operations**: Some scripts (unused-disks.py, delete-unused-ips.py) will permanently delete resources
- **No Confirmation Prompts**: Scripts execute immediately without user confirmation
- **Zone vs Region**: Some scripts use zones (unused-disks.py, shutdown-vms.py) while others use regions (delete-unused-ips.py)
- **Error Handling**: All scripts include basic error handling but may need enhancement for production use

## 🔧 Troubleshooting

### Common Issues:

1. **Authentication Errors**: Ensure your service account key is properly set or gcloud is authenticated
2. **Permission Denied**: Verify your service account has the required IAM roles
3. **Project Not Found**: Double-check your `GCP_PROJECT_ID` environment variable
4. **Zone/Region Mismatch**: Ensure the zone/region exists in your project

### Debug Mode:
Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to your service account key:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"
```

## 📝 Contributing

When adding new scripts:
1. Follow the existing code structure and error handling patterns
2. Include proper environment variable validation
3. Add comprehensive documentation in this README
4. Update requirements.txt if new dependencies are needed
5. Test thoroughly before submitting

## 📄 License

This project is for internal use. Please ensure compliance with your organization's policies and Google Cloud Platform terms of service.
