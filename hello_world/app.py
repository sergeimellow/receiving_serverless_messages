import json
import boto3
import time
import base64

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('serge_messages')

def lambda_handler(event, context):
    message_time_received = str(time.time())
    print("the event:")
    print(event)
    print("the context:")
    print(context)
    print("Hello World was called at " + message_time_received + " epoch time" )

    # get message if present
    message = event['queryStringParameters']['message'] if event.get("queryStringParameters") and event['queryStringParameters'].get('message') else ''

    if message == "":
        return {
            "statusCode": 400,
            "body": "BAD REQUEST: missing query paramter named 'message', example: .../hello?message=your-message"
        }
    else:
        # generate unique primary key
        message_pk = message_time_received + message
        message_pk_bytes = message_pk.encode("ascii")
        message_pk_base64_bytes = base64.b64encode(message_pk_bytes)
        message_pk_hashed = message_pk_base64_bytes.decode("ascii")

        table.put_item(
            Item={
                "id": message_pk_hashed,
                "time_received": message_time_received,
                "message": message 
            }
        )


        return {
            "statusCode": 200,
            "body": "You sent the message '" + message + "' to serge's lambda function that saved it to a dynamoDB table"
        }
