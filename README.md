Automatic EBS Snapshot and Cleanup Using AWS Lambda

## Objective
To automate the backup of Amazon EBS volumes by creating snapshots using AWS Lambda and to clean up old snapshots beyond a defined retention period to optimize storage costs.

---

## AWS Services Used
- Amazon EC2 (EBS Volumes & Snapshots)
- AWS Lambda
- AWS IAM
- Amazon CloudWatch
- Amazon EventBridge (optional / bonus)

---

## Architecture Overview
- An AWS Lambda function is triggered manually or on a schedule.
- The function creates an EBS snapshot for a specified volume.
- It scans existing snapshots owned by the account.
- Snapshots older than the retention period are deleted.
- Snapshots linked to AMIs are safely skipped to avoid errors.

---

## EBS Setup
- An existing EBS volume attached to an EC2 instance was identified.
- The Volume ID was used as input for snapshot creation.

---

## IAM Role
- A dedicated IAM role was created for the Lambda function.
- Policy attached: `AmazonEC2FullAccess` (used for simplicity as per assignment instructions).

---

## Lambda Function Details
- Runtime: Python 3.x
- The function performs the following actions:
  1. Creates a snapshot for the specified EBS volume.
  2. Identifies snapshots older than 30 days.
  3. Deletes old snapshots.
  4. Skips snapshots that are associated with AMIs.
  5. Logs snapshot creation and cleanup actions.

---

## Manual Invocation
- The Lambda function was manually triggered using a test event.
- Execution status was verified as successful.
- CloudWatch logs were reviewed for snapshot creation and cleanup actions.

---

## Testing Notes
- Snapshot creation was confirmed in the EC2 Snapshots console.
- Cleanup logic safely skipped snapshots in use by AMIs.
- No errors occurred during execution.

---

## Result
- New EBS snapshots were created automatically.
- Old snapshots were cleaned up according to the retention policy.
- AMI-linked snapshots were preserved to prevent failures.

---

## Conclusion
This assignment demonstrates a real-world AWS automation use case for backup management, retention enforcement, and cost optimization using AWS Lambda and Boto3.

## Screenshots
- Volume 
<img width="1440" height="900" alt="Screenshot 2025-12-23 at 13 39 22" src="https://github.com/user-attachments/assets/7a2aba75-a305-4640-b60b-e7448adcd440" />

- IAM role
<img width="1440" height="900" alt="Screenshot 2025-12-23 at 13 45 53" src="https://github.com/user-attachments/assets/6be9dfe6-baeb-493a-bd1e-6204c79a53c8" />

- Terminal Output
<img width="1440" height="900" alt="Screenshot 2025-12-23 at 13 47 57" src="https://github.com/user-attachments/assets/6adfe741-84ef-4c96-83a3-1b7ed668f578" />

- Config Timeout
<img width="1464" height="928" alt="Screenshot 2025-12-23 at 13 48 53" src="https://github.com/user-attachments/assets/27ec6c30-5645-4fe5-832f-ae70bee403f8" />
