# Opportunity Calendar - Deployment Guide

## Step 1: Verify DynamoDB Table Schema

### 1.1 Check Your Existing Table
1. Go to **DynamoDB** → **Tables**
2. Find your existing calendar table
3. **🚨 CRITICAL:** Verify the **Primary key** is `EventID` (String type)
4. **📝 NOTE YOUR TABLE NAME** - you'll need this for the CloudFormation stack

### 1.2 Fix Schema if Needed
If your table doesn't have `EventID` as the primary key:
1. **Option A:** Create a new table with correct schema
2. **Option B:** Export data, delete table, recreate with correct schema, import data
3. **Primary key must be:** `EventID` (String)

---

## Step 2: Create SNS Topic for Email Notifications

### 2.1 Create the SNS Topic
1. Go to **AWS SNS** in the console
2. Click **Topics** → **Create topic**
3. Select **Standard** type
4. Name: `student-event-notifications` (or your preferred name)
5. Click **Create topic**
6. **📝 COPY THE TOPIC ARN** - you'll need this later!
   - Format: `arn:aws:sns:YOUR-REGION:YOUR-ACCOUNT:student-event-notifications`

### 2.2 Subscribe to Email Notifications
1. In your new SNS topic, click **Create subscription**
2. Protocol: **Email**
3. Endpoint: **Your email address**
4. Click **Create subscription**
5. Check your email and **confirm the subscription**

---

## Step 3: Deploy the Calendar API Infrastructure

### 3.1 Deploy CloudFormation Stack
1. Go to **CloudFormation** → **Create stack**
2. Choose **Upload a template file**
3. Upload the `opp-cal-cfn.yaml` file
4. Stack name: `student-calendar-api`
5. **🚨 CRITICAL:** Change the **DynamoDBTableName** parameter to **YOUR ACTUAL TABLE NAME**
   - Default is `opp-calendar-table`
   - Replace with your existing table name
6. Click **Next** through remaining pages and **Create stack**
7. Wait for stack creation to complete
8. Go to **Outputs** tab and **📝 COPY the APIEndpoint URL**
   - Format: `https://XXXXXXXX.execute-api.YOUR-REGION.amazonaws.com/prod`

---

## Step 4: Configure Lambda Function

You have two options for the Lambda function:

### Option A: Update Your Existing Lambda Function (Recommended)

#### 4A.1 Update Existing Function
1. Go to **AWS Lambda** → **Functions**
2. Select your **existing Lambda function**
3. In the code editor, **replace all existing code** with the contents of `lambda_function.py`
4. **🚨 CRITICAL: Update these variables in the code:**
   ```python
   # Line ~66: Update with YOUR API Gateway URL from Step 3.1
   api_base_url = "https://YOUR-API-ID.execute-api.YOUR-REGION.amazonaws.com/prod"
   
   # Line ~70: Update with YOUR SNS Topic ARN from Step 2.1
   SNS_TOPIC_ARN = 'arn:aws:sns:YOUR-REGION:YOUR-ACCOUNT:student-event-notifications'
   ```
5. Click **Deploy** to save changes
6. **Continue to Step 4.3** for permissions

### Option B: Create New Lambda Function

#### 4B.1 Create New Lambda Function
1. Go to **AWS Lambda** → **Create function**
2. Choose **Author from scratch**
3. Function name: `student-calendar-handler`
4. Runtime: **Python 3.9** or **Python 3.11**
5. Click **Create function**

#### 4B.2 Update New Lambda Code
1. In the Lambda function, replace the default code with `lambda_function.py`
2. **🚨 CRITICAL: Update these variables in the code:**
   ```python
   # Line ~66: Update with YOUR API Gateway URL from Step 3.1
   api_base_url = "https://YOUR-API-ID.execute-api.YOUR-REGION.amazonaws.com/prod"
   
   # Line ~70: Update with YOUR SNS Topic ARN from Step 2.1
   SNS_TOPIC_ARN = 'arn:aws:sns:YOUR-REGION:YOUR-ACCOUNT:student-event-notifications'
   ```
3. Click **Deploy** to save changes

### 4.3 Update Lambda Execution Role (Required for Both Options)
1. In your Lambda function, go to **Configuration** → **Permissions**
2. Click on the **Execution role name** (opens in new tab)
3. Click **Add permissions** → **Create inline policy**
4. Use the **JSON** editor and paste:
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "sns:Publish"
         ],
         "Resource": "arn:aws:sns:YOUR-REGION:YOUR-ACCOUNT:student-event-notifications"
       }
     ]
   }
   ```
5. **🚨 CRITICAL: Replace with YOUR actual SNS Topic ARN**
6. Name the policy: `SNSPublishPolicy`
7. **Create policy**

---

## Step 5: Configure Bedrock Agent

### 5.1 Update Agent Action Group
1. Go to **Amazon Bedrock** → **Agents**
2. Select your existing agent
3. Go to **Action groups** section
4. Edit your existing action group or create a new one:
   - Name: `calendar-actions`
   - Type: **API Schema**

### 5.2 Connect Lambda Function
1. In the action group configuration:
   - **Lambda function**: Select your Lambda function (existing updated one OR new one)
   - **Action group schema**: Select **Define with API schemas**
   
### 5.3 Add API Schema
1. Copy the contents of `api-for-action-group.yaml`
2. **🚨 CRITICAL: Update the server URL in the YAML:**
   ```yaml
   servers:
     - url: https://YOUR-API-ID.execute-api.YOUR-REGION.amazonaws.com/prod
       description: Production server
   ```
3. Paste the updated YAML into the **API Schema** field
4. **Save** the action group

---

## Step 6: Add Bedrock Permissions to Lambda

### 6.1 Add Resource-Based Policy
1. Go to your **Lambda function** (whichever one you chose in Step 4)
2. Click **Configuration** → **Permissions**
3. Scroll to **Resource-based policy statements**
4. Click **Add permissions**
5. Fill in:
   - **Statement ID**: `BedrockInvokePermission`
   - **Principal**: `bedrock.amazonaws.com`
   - **Source ARN**: `arn:aws:bedrock:YOUR-REGION:YOUR-ACCOUNT:agent/YOUR-AGENT-ID`
   - **Action**: `lambda:InvokeFunction`
6. **🚨 CRITICAL: Replace YOUR-AGENT-ID with your actual Bedrock Agent ID**
7. Click **Save**

### 6.2 Find Your Bedrock Agent ID
- Go to **Bedrock** → **Agents** → Select your agent
- The Agent ID is in the **Agent overview** section
- Format: `ABCDEFGHIJ`

---

## Step 7: Prepare and Test Your Agent

### 7.1 Prepare Agent for Testing
1. In **Bedrock Agents**, select your agent
2. Click **Prepare** (this may take a few minutes)
3. Wait for status to show **Prepared**

### 7.2 Test the Complete System

#### Test 1: API Gateway (Optional)
1. Go to **API Gateway** → Your calendar API
2. Click **Test** → **POST** → `/events`
3. Test with sample data:
   ```json
   {
     "EventID": "test-001",
     "EventName": "Test Event",
     "StartDateTime": "2024-03-15 2:00 PM",
     "Location": "Test Location",
     "Campus": "Main Campus"
   }
   ```

#### Test 2: Lambda Function
1. In **Lambda**, go to your function → **Test** tab
2. Click **Create new event**
3. Event name: `BedrockAgentTest`
4. Use this test event JSON:

```json
{
  "messageVersion": "1.0",
  "agent": {
    "name": "StudentEventAgent",
    "version": "1.0",
    "id": "ABCDEFGHIJ",
    "alias": "TSTALIASID"
  },
  "inputText": "Save this event to my calendar",
  "sessionId": "session-123",
  "actionGroup": "calendar-actions",
  "apiPath": "/events",
  "httpMethod": "POST",
  "parameters": [],
  "requestBody": {
    "content": {
      "application/json": {
        "properties": [
          {
            "name": "EventID",
            "type": "string",
            "value": "test-event-123"
          },
          {
            "name": "EventName",
            "type": "string",
            "value": "Tech Industry Networking Night"
          },
          {
            "name": "StartDateTime",
            "type": "string",
            "value": "March 15, 2024, 6:00 PM"
          },
          {
            "name": "Location",
            "type": "string",
            "value": "Student Union Building, Grand Ballroom"
          },
          {
            "name": "Campus",
            "type": "string",
            "value": "Main Campus"
          },
          {
            "name": "EventType",
            "type": "string",
            "value": "Networking Event"
          },
          {
            "name": "Organizer",
            "type": "string",
            "value": "Career Services Department"
          },
          {
            "name": "Description",
            "type": "string",
            "value": "Join us for an exclusive networking evening designed specifically for Computer Science and Engineering students."
          },
          {
            "name": "Time",
            "type": "string",
            "value": "6:00 PM - 9:30 PM"
          }
        ]
      }
    }
  }
}
```

5. Click **Test**
6. Check the response and **CloudWatch logs**
7. **Check your email** for the notification!
8. **Check DynamoDB** to verify the item was created

#### Test 3: End-to-End with Bedrock Agent
1. Go to your **Bedrock Agent** → **Test**
2. Try these queries:
   - "What entrepreneurship events are available?"
   - "I'd like to save the startup workshop to my calendar"
   - "Show me my saved events"
3. **Check your email** for notifications when events are saved!

---

## Troubleshooting Checklist

### Common Issues:

#### DynamoDB Schema Problems:
- ✅ Primary key is `EventID` (String type)
- ✅ Table name in CloudFormation matches your actual table
- ✅ CloudFormation stack deployed successfully

#### If the agent isn't finding events:
- ✅ Knowledge base is properly configured
- ✅ Agent instructions distinguish between knowledge base and calendar
- ✅ Agent is **Prepared** after changes

#### If calendar saving fails:
- ✅ API Gateway URL is correct in Lambda function
- ✅ Lambda execution role has DynamoDB permissions (added by CloudFormation)
- ✅ DynamoDB table name matches in CloudFormation parameter
- ✅ Correct Lambda function is connected to Bedrock agent

#### If email notifications don't work:
- ✅ SNS Topic ARN is correct in Lambda function
- ✅ Lambda has SNS publish permissions
- ✅ Email subscription is confirmed
- ✅ Check Lambda logs for SNS errors

#### If Bedrock can't invoke Lambda:
- ✅ Resource-based policy is added to the correct Lambda function
- ✅ Bedrock Agent ARN is correct in the policy
- ✅ Agent is prepared after configuration changes
- ✅ Correct Lambda function is selected in Bedrock action group

#### Lambda Test Failures:
- ✅ Check CloudWatch logs for detailed error messages
- ✅ Verify API Gateway URL is accessible
- ✅ Confirm SNS topic exists and ARN is correct

---

## Key Variables to Update Summary

| File/Location | Variable | What to Update |
|---------------|----------|----------------|
| CloudFormation Parameter | `DynamoDBTableName` | Your existing DynamoDB table name |
| `lambda_function.py` | `api_base_url` | Your API Gateway URL |
| `lambda_function.py` | `SNS_TOPIC_ARN` | Your SNS Topic ARN |
| `api-for-action-group.yaml` | `servers[0].url` | Your API Gateway URL |
| Lambda IAM Policy | `Resource` | Your SNS Topic ARN |
| Lambda Resource Policy | `Source ARN` | Your Bedrock Agent ARN |
| Bedrock Agent Action Group | Lambda function selection | Your chosen Lambda function |

---

## Success Indicators

✅ **CloudFormation**: Stack creates successfully with your table name  
✅ **API Gateway**: Returns 201 for POST requests  
✅ **Lambda Test**: Test event executes successfully with proper response  
✅ **Lambda Logs**: Show successful API calls and SNS publishing  
✅ **DynamoDB**: Items appear in your existing table  
✅ **SNS**: Email notifications arrive  
✅ **Bedrock Agent**: Responds appropriately to calendar requests  
