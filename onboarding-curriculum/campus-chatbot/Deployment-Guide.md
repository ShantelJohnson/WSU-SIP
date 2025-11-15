# Chatbot Deployment Guide

This guide will help you set up and deploy the backend, knowledge base synchronization, and frontend integration for the Campus Chatbot.

---

## Backend Setup

### 1. Replace Lambda Function Code

- ⚠️ **Critical Steps**:
   - Ensure the KNOWLEDGE_BASE_ID is correct (this information can be found in the Amazon Bedrock Console --> Build --> Knowledge Bases).
   - Ensure the model ARN is correct and uses the inference profile ID for Nova Pro (Amazon Bedrock Console --> Infer --> Cross-region Inference).


### 2. Confirm IAM Permissions

- Run a test event. If you encounter a permissions error, Lambda may not have access to Bedrock.

**Simple Test Event**:
```json
{
  "body": "{\"message\": \"Can you tell me about networking events?\"}",
  "httpMethod": "POST",
  "headers": {
    "Content-Type": "application/json"
  },
  "isBase64Encoded": false
}
```

- **To update permissions**:
  - Go to the IAM console [IAM Console](https://console.aws.amazon.com/iam/).
  - Find the Lambda execution role.
  - Attach a policy allowing `bedrock:InvokeModel`.

### 3. Confirm No Timeout Issues

- Use the same test event. If there's a timeout error, update the Lambda function's timeout setting.
- **To change the timeout**:
  - Go to the Lambda console [Lambda Console](https://console.aws.amazon.com/lambda/).
  - Select your function.
  - In the "Configuration" tab, adjust the timeout under "General configuration".

### 4. Deploy CloudFormation Template (API)

- **Console Instructions**:
  - Open the CloudFormation console [CloudFormation Console](https://console.aws.amazon.com/cloudformation/).
  - Click "Create stack" and upload `chatbot-api-cfn.yaml`.
  - Enter the stack name and parameters, ensuring `LambdaFunctionName` matches your actual Lambda function.

### 5. Find and Test the API in API Gateway

- **Locate the API**:
  - Go to the API Gateway console [API Gateway Console](https://console.aws.amazon.com/apigateway/).
  - Find the API created by the CloudFormation stack.

- **Test the POST Method**:
  - Select the API and go to the "/chat" resource.
  - Click on the "POST" method and then "Test".
  - Use the following example event:

```json
{
  "message": "Can you tell me about networking events?"
}
```

---

## Knowledge Base Sync

### 1. Deploy the CloudFormation Template

- **Console Instructions**:
  - Open the CloudFormation console [CloudFormation Console](https://console.aws.amazon.com/cloudformation/).
  - Click "Create stack" and upload `kb-refresh-cfn.yaml`.
  - Enter the stack name and parameters, replacing `KnowledgeBaseId` and `DataSourceId` with actual values.

- ⚠️ **Critical Step**: If you have multiple source IDs, deploy the template for each one.

**Test Event (for knowledge base lambda function)**:
```json
{
  "knowledge_base_id": "SFKHOELRRK",
  "dataSourceId": "Y1HYKSQYIU"
}
```

---

## Frontend Integration

### 1. Validate Frontend

- Ensure the UI displays correctly in the web browser.

### 2. Add Script to HTML

- The purpose of this step is to add a script to your HTML page that will allow it to communicate with the backend API. This script sends user messages to the backend and handles the responses.

### 3. Test Full App Integration

- Run the following test in a terminal (local or CloudShell):

```bash
API_URL="https://XXXX.execute-api.YOUR-AWS-REGION.amazonaws.com/prod/chat"

# Test with a simple question
curl -X POST $API_URL \
  -H "Content-Type: application/json" \
  -d '{"message": "Can you tell me about networking events?"}'
```

- ⚠️ **Critical Step**: Ensure the API_URL is the actual URL found in API Gateway.
