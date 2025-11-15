import json
import urllib3
import uuid
import boto3  # Added for SNS

def lambda_handler(event, context):
    print(f"=== BEDROCK AGENT EVENT DEBUG ===")
    print(f"Full event: {json.dumps(event, indent=2)}")
    
    # Extract required fields
    api_path = event.get('apiPath', '')
    http_method = event.get('httpMethod', '')
    action_group = event.get('actionGroup', '')
    
    # Extract parameters from the request body structure
    request_body = event.get('requestBody', {})
    parameters = event.get('parameters', [])
    
    print(f"Request body field: {request_body}")
    print(f"Parameters field: {parameters}")
    
    # Build params_dict from the request body structure
    params_dict = {}
    
    # Method 1: Extract from requestBody.content.application/json.properties (list format)
    if request_body and 'content' in request_body:
        content = request_body['content']
        if 'application/json' in content:
            json_content = content['application/json']
            if 'properties' in json_content:
                properties = json_content['properties']
                print(f"Properties found: {properties}")
                
                # Properties is a list of objects with name, type, and value
                if isinstance(properties, list):
                    print("Processing properties as list")
                    for prop in properties:
                        if isinstance(prop, dict) and 'name' in prop and 'value' in prop:
                            params_dict[prop['name']] = prop['value']
                            print(f"Added from properties: {prop['name']} = {prop['value']}")
                
                # Fallback: if properties is somehow a dict
                elif isinstance(properties, dict):
                    print("Processing properties as dict")
                    for key, value in properties.items():
                        if isinstance(value, dict) and 'value' in value:
                            params_dict[key] = value['value']
                        else:
                            params_dict[key] = value
                        print(f"Added from properties dict: {key} = {params_dict[key]}")
    
    # Method 2: Fallback to parameters field if requestBody didn't work
    if not params_dict and isinstance(parameters, list):
        print("Fallback: Processing parameters as list")
        for param in parameters:
            if isinstance(param, dict) and 'name' in param and 'value' in param:
                params_dict[param['name']] = param['value']
                print(f"Added from parameters: {param['name']} = {param['value']}")
    
    print(f"Final parsed params_dict: {json.dumps(params_dict, indent=2)}")
    
    # Generate EventID if missing
    if 'EventID' not in params_dict or not params_dict.get('EventID'):
        params_dict['EventID'] = f"event-{str(uuid.uuid4())[:8]}"
        print(f"Generated EventID: {params_dict['EventID']}")
    
    # Your API Gateway URL
    api_base_url = "https://YOUR_API_GATEWAY_ID.execute-api.YOUR_REGION.amazonaws.com/YOUR_STAGE"  # UPDATE THIS
    
    # Initialize SNS client
    sns = boto3.client('sns')
    SNS_TOPIC_ARN = 'arn:aws:sns:YOUR_REGION:YOUR_ACCOUNT_ID:YOUR_TOPIC_NAME'  # UPDATE THIS
    
    http = urllib3.PoolManager()
    
    try:
        if api_path == "/events" and http_method == "POST":
            # Map the params to your expected event structure
            event_data = {
                'EventID': params_dict.get('EventID', ''),
                'Campus': params_dict.get('Campus', ''),
                'StartDateTime': params_dict.get('StartDateTime', ''),
                'Description': params_dict.get('Description', ''),
                'EventName': params_dict.get('EventName', ''),
                'EventType': params_dict.get('EventType', ''),
                'Location': params_dict.get('Location', ''),
                'Organizer': params_dict.get('Organizer', ''),
                'Time': params_dict.get('Time', '')
            }
            
            request_payload = json.dumps(event_data)
            print(f"Making POST request to: {api_base_url}/events")
            print(f"Request payload: {request_payload}")
            
            response = http.request(
                'POST',
                f"{api_base_url}/events",
                body=request_payload,
                headers={'Content-Type': 'application/json'}
            )
            
            print(f"API Response - Status: {response.status}")
            print(f"API Response - Body: {response.data.decode('utf-8')}")
            
            if response.status in [200, 201]:
                result = json.loads(response.data.decode('utf-8'))
                event_name = event_data.get('EventName', 'Unknown Event')
                event_time = event_data.get('StartDateTime', 'TBD')
                event_location = event_data.get('Location', 'TBD')
                
                # Send SNS notification
                try:
                    message = f"""New Event Added to Your Calendar!

Event: {event_name}
Date/Time: {event_time}
Location: {event_location}

You're all set! We'll send you a reminder closer to the event date.

Event ID: {event_data.get('EventID')}"""
                    
                    subject = f"{event_name} added to your calendar"
                    
                    sns_response = sns.publish(
                        TopicArn=SNS_TOPIC_ARN,
                        Message=message,
                        Subject=subject
                    )
                    
                    print(f"SNS notification sent successfully: {sns_response['MessageId']}")
                    
                except Exception as sns_error:
                    print(f"Failed to send SNS notification: {str(sns_error)}")
                    # Don't fail the whole operation if SNS fails
                
                response_text = f"Successfully saved '{event_name}' to your calendar! EventID: {event_data.get('EventID')}"
                
            else:
                error_body = response.data.decode('utf-8')
                response_text = f"Failed to save event. Status: {response.status}. Error: {error_body}"
                
        elif api_path == "/events" and http_method == "GET":
            print(f"Making GET request to: {api_base_url}/events")
            response = http.request('GET', f"{api_base_url}/events")
            
            print(f"GET Response - Status: {response.status}")
            print(f"GET Response - Body: {response.data.decode('utf-8')}")
            
            if response.status == 200:
                result = json.loads(response.data.decode('utf-8'))
                events = result.get('events', [])
                count = result.get('count', 0)
                
                if count > 0:
                    response_text = f"You have {count} events saved to your calendar:\n"
                    for event_item in events:
                        event_name = event_item.get('EventName', 'N/A')
                        event_date = event_item.get('StartDateTime', 'N/A')
                        event_location = event_item.get('Location', 'N/A')
                        response_text += f"• {event_name} - {event_date} at {event_location}\n"
                else:
                    response_text = "You don't have any events saved to your calendar yet."
            else:
                error_body = response.data.decode('utf-8')
                response_text = f"Failed to retrieve your events. Status: {response.status}. Error: {error_body}"
        else:
            response_text = f"Unsupported request: {http_method} {api_path}"
            
        return {
            "messageVersion": "1.0",
            "response": {
                "actionGroup": action_group,
                "apiPath": api_path,
                "httpMethod": http_method,
                "httpStatusCode": 200,
                "responseBody": {
                    "TEXT": {
                        "body": response_text
                    }
                }
            }
        }
        
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        import traceback
        print(f"Full traceback: {traceback.format_exc()}")
        
        return {
            "messageVersion": "1.0",
            "response": {
                "actionGroup": action_group,
                "apiPath": api_path,
                "httpMethod": http_method,
                "httpStatusCode": 500,
                "responseBody": {
                    "TEXT": {
                        "body": f"Internal error: {str(e)}"
                    }
                }
            }
        }
