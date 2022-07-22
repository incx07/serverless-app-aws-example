import json
import boto3


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Announcement')


def lambda_handler(event, context):
    """Lambda function for listing all announcements

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
        response = table.scan()
    except Exception as ex:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(ex)
            }),
        }        
    else:  
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": response.get('Items', {}),
            }),
        }
