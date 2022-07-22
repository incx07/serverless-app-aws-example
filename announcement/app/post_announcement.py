import json
import boto3
from uuid import uuid4


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Announcement')


def lambda_handler(event, context):
    """Lambda function for adding a new Announcement to the system

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format
    context: object, required
        Lambda Context runtime methods and attributes

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

    """
    try:
        body = json.loads(event['body'])
        new_item = {
            'uid': str(uuid4()),
            'title': body.get('title', ''), 
            'description': body.get('description', ''), 
            'date': body.get('date', ''), 
        }
        response = table.put_item(Item=new_item)
    except Exception as ex:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(ex)
            }),
        }
    else:   
        return {
            'statusCode': 200,
            'body': json.dumps(response),
        }

