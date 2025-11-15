import json
import boto3
import logging
from botocore.exceptions import ClientError

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize Bedrock client
bedrock_agent_runtime = boto3.client('bedrock-agent-runtime')

# Configuration
KNOWLEDGE_BASE_ID = "UPDATE_ME" # Update with your actual Knowledge Base ID
MODEL_ARN = "us.amazon.nova-pro-v1:0"  # ← This is the inference profile ID

def lambda_handler(event, context):
    try:
        # Extract user message from event
        if 'body' in event:
            body = json.loads(event['body'])
            user_message = body.get('message', '')
        else:
            user_message = event.get('message', '')
        
        if not user_message:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'No message provided'})
            }
        
        logger.info(f"Processing user message: {user_message}")
        
        # Use inference profile ID
        response = bedrock_agent_runtime.retrieve_and_generate(
            input={
                'text': user_message
            },
            retrieveAndGenerateConfiguration={
                'type': 'KNOWLEDGE_BASE',
                'knowledgeBaseConfiguration': {
                    'knowledgeBaseId': KNOWLEDGE_BASE_ID,
                    'modelArn': MODEL_ARN  # This is now the inference profile ID
                }
            }
        )
        
        generated_text = response['output']['text']
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'response': generated_text,
                'knowledgeBaseId': KNOWLEDGE_BASE_ID,
                'model': 'us.amazon.nova-pro-v1:0'
            })
        }
        
    except ClientError as e:
        error_code = e.response['Error']['Code']
        error_message = e.response['Error']['Message']
        
        logger.error(f"AWS Client Error: {error_code} - {error_message}")
        
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': f"AWS Error: {error_code}",
                'message': error_message
            })
        }
        
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Internal server error',
                'message': str(e)
            })
        }
