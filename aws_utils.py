import boto3
from config import AWS_CONFIG

def upload_to_s3(file_name, bucket, object_name=None):
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_CONFIG['aws_access_key_id'],
        aws_secret_access_key=AWS_CONFIG['aws_secret_access_key']
    )
    object_name = object_name or file_name
    s3.upload_file(file_name, bucket, object_name)
    return f"https://{bucket}.s3.amazonaws.com/{object_name}"