import boto3
from datetime import datetime, timezone, timedelta
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    VOLUME_ID = "vol-08e61be3bb3c0a972"  # your volume
    RETENTION_DAYS = 30

    # 1️⃣ Create snapshot
    snapshot = ec2.create_snapshot(
        VolumeId=VOLUME_ID,
        Description="Automated snapshot via Lambda"
    )
    print(f"Created snapshot: {snapshot['SnapshotId']}")

    # 2️⃣ Cleanup old snapshots
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=RETENTION_DAYS)

    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']

    for snap in snapshots:
        if snap['StartTime'] < cutoff_date:
            try:
                ec2.delete_snapshot(SnapshotId=snap['SnapshotId'])
                print(f"Deleted snapshot: {snap['SnapshotId']}")
            except ClientError as e:
                if e.response['Error']['Code'] == 'InvalidSnapshot.InUse':
                    print(f"Skipping snapshot in use by AMI: {snap['SnapshotId']}")
                else:
                    raise e

    return {
        "statusCode": 200,
        "body": "EBS snapshot creation and cleanup completed"
    }
