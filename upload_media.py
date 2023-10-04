# upload_media.py

import ibm_boto3
from ibm_botocore.client import Config
import os

def main(args):
    cos_api_key = os.environ.get('COS_API_KEY_ID')
    cos_service_instance_id = os.environ.get('COS_RESOURCE_CRN')
    cos_endpoint = args.get('endpoint')
    cos_bucket = args.get('bucket')

    cos = ibm_boto3.client('s3',
        ibm_api_key_id=cos_api_key,
        ibm_service_instance_id=cos_service_instance_id,
        config=Config(signature_version='oauth'),
        endpoint_url=cos_endpoint
    )

    media_file = args.get('media_file')
    media_filename = media_file.filename
    media_file_data = media_file.file.read()

    cos.upload_fileobj(
        Fileobj=media_file_data,
        Bucket=cos_bucket,
        Key=media_filename
    )

    return {
        'message': f'Successfully uploaded {media_filename} to {cos_bucket}'
    }
