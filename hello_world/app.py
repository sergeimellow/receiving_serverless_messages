import json

# import requests


def lambda_handler(event, context):
    print(event)
    print(context)
    message = event['queryStringParameters']['message'] if event['queryStringParameters'] && event['queryStringParameters']['message']

    return {
        "statusCode": 200,
        "body": json.dumps({
            "You sent the message" + message + " to serge's lambda function that saved it in dynamoDB" ,
        }),
    }
