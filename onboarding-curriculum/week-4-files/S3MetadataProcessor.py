import json
import boto3
import os
import datetime
from decimal import Decimal
import urllib.parse

# Initialize AWS clients
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

# TODO: Replace with your actual DynamoDB table name
TABLE_NAME = "YOUR_DYNAMODB_TABLE_NAME"

def lambda_handler(event, context):
    """
    Lambda function that extracts metadata from S3 objects and stores it in DynamoDB
    
    Parameters:
        event: The event dict containing the S3 event details
        context: Lambda context object
    
    Returns:
        JSON response indicating success or failure
    """
    try:
        # TODO: Extract bucket name and object key from the event
        # Hint: The information is nested in the event object under 'Records'
        bucket_name = "???" # Fix this line
        object_key = "???"  # Fix this line
        
        print(f"Processing object: {object_key} in bucket: {bucket_name}")
        
        # Get object metadata from S3
        # TODO: Call the appropriate S3 client method to get object details
        response = ??? # Complete this line
        
        # Prepare item for DynamoDB
        # Note: DynamoDB doesn't support Python's datetime objects or float values directly
        timestamp = response['LastModified'].isoformat()
        
        item = {
            'object_key': object_key,
            'bucket_name': bucket_name,
            'size': Decimal(str(response['ContentLength'])),
            'last_modified': timestamp,
            'etag': response['ETag'].strip('"'),
            'content_type': response.get('ContentType', 'unknown'),
            # TODO: Extract any custom metadata from the response and add it to the item
            'processed_date': datetime.datetime.now().isoformat()
        }
        
        # TODO: Get the DynamoDB table and put the item into it
        table = ???  # Complete this line
        result = ??? # Complete this line - put the item into the table
        
        print(f"Successfully recorded metadata for {object_key}")
        
        return {
            'statusCode': 200,
            'body': json.dumps('Object metadata successfully stored in DynamoDB')
        }
        
    except Exception as e:
        print(f"Error processing object: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
