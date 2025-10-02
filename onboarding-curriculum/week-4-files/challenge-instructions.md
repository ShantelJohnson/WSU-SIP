# S3 to DynamoDB Metadata Challenge

## Challenge Overview

In this exercise, you will build a serverless application that automatically extracts metadata from files uploaded to Amazon S3 and stores this information in Amazon DynamoDB. This represents a common pattern in cloud applications where object storage events trigger downstream processing.

## Learning Objectives

- Create and configure AWS resources (S3, DynamoDB, Lambda)
- Complete a partially implemented Lambda function
- Set up event-driven workflows using S3 event notifications
- Use generative AI to help solve coding problems

## Setup Instructions

### 1. Create an S3 Bucket

[TODO]

### 2. Create a DynamoDB Table

[TODO]

**Note:** For the partition key, use `object_key` (String) - this must match exactly what's used in the Lambda code

### 3. Create a Lambda Function

1. Navigate to Lambda in the AWS Console
2. Click "Create function"
3. Choose "Author from scratch"
4. Name your function (e.g., S3MetadataProcessor)
5. Select Python 3.9 or later as the runtime
6. Under "Permissions", select "Create a new role with basic Lambda permissions"
7. Click "Create function"
8. Replace the default code with the provided partial code

### 4. Complete the Lambda Code

Use the provided code template and fill in the missing parts marked with TODO comments and ???:

- Extract bucket name and object key from the event
- Call the appropriate S3 client method to get object metadata
- Get the DynamoDB table reference
- Put the item into the DynamoDB table

### 5. Configure Lambda Permissions

1. In your Lambda function page, go to the "Configuration" tab
2. Select "Permissions"
3. Click on the execution role
4. In the IAM console, add permissions for: 
   - S3 read access (to get metadata)
   - DynamoDB write access (to store metadata)
   - CloudWatch Logs (for debugging)

You can use the AWS managed policies `AmazonS3ReadOnlyAccess` and `AmazonDynamoDBFullAccess` for this challenge

### 6. Set Up S3 Event Notification

[TODO]

## Testing Your Solution

1. Upload a file to your S3 bucket
2. Check CloudWatch Logs for your Lambda function to ensure it ran without errors
3. Navigate to your DynamoDB table and verify that the metadata was stored correctly

## Troubleshooting Tips

- If your function fails, check the CloudWatch Logs for error messages
- Copy any error messages into Amazon Q Developer chat for help understanding and resolving the issue
- Common issues include: 
  - Incorrect permission settings (IAM role)
  - Incorrectly formatted event data extraction
  - Syntax errors in the Python code

## Hint for Completing the Challenge

Remember, you can use Amazon Q Developer (and the Bedrock Chat Playground) to help you understand any part of the code that's unclear or to troubleshoot errors you encounter!

## Helpful Prompts for AWS GenAI Challenge

Here are various prompts students can use with Amazon Q Developer to help solve the S3 to DynamoDB metadata challenge:

### Understanding the Challenge

- "Can you explain what this Lambda function is trying to do at a high level?"
- "Walk me through how S3 event notifications work with Lambda functions"
- "What's the relationship between S3, Lambda, and DynamoDB in this serverless pattern?"

### Code Completion Help

- "How do I extract the bucket name and object key from an S3 event in Lambda?"
- "Show me how to put an item into a DynamoDB table using boto3"

### Error Understanding & Troubleshooting

- "I'm getting this error: [paste error]. Can you explain what it means and how to fix it?"
- "Why am I getting a permission error when my Lambda tries to access S3/DynamoDB?"
- "My Lambda function is timing out. How can I diagnose and fix this issue?"
- "I'm seeing 'TypeError: Object of type datetime is not JSON serializable'. How do I fix this?"

## Time Expectations

This challenge is designed to be completed in approximately 2-3 hours. Remember that learning to use generative AI effectively for technical problem-solving is part of the challenge!

If you find yourself spending more than 15-20 minutes stuck on a single step:

- Try formulating a different prompt for Q Developer (or the Bedrock Chat Playground)
- Review the AWS documentation for the specific service you're working with
  - [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
  - [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
  - [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
  - [Amazon CloudWatch] (https://docs.aws.amazon.com/lambda/latest/dg/python-logging.html#python-logging-cwconsole)

- Ask for guidance

**Note on [TODO] Sections:** Some parts of this guide are intentionally marked as [TODO]. Use these as opportunities to practice researching with Q Developer or the AWS documentation. For example, you could ask Q Developer: "What are the steps to create an S3 bucket in AWS?"
