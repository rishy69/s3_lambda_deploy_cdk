import json
import boto3
import os

def lambda_handler(event, context):
    # Get the bucket name from environment variable
    bucket_name = os.environ['BUCKET_NAME']
    
    # Create S3 client
    s3_client = boto3.client('s3')
    
    try:
        # Example: List objects in the bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Lambda function executed successfully',
                'bucket': bucket_name,
                'object_count': response.get('KeyCount', 0)
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }