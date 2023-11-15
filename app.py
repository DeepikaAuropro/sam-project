import json
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = 'UserRegistrationTable'
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        # Check if 'body' is present in the Lambda event
        if 'body' not in event or event['body'] is None:
            raise ValueError('Request body is missing')

        # Parse registration data from the Lambda event
        body = json.loads(event['body'])
        user_name = body['user_name']
        email = body['email']

        # Store data in DynamoDB
        table.put_item(
            Item={
                'user_name': user_name,
                'email': email
            }
        )

        

        # Return a successful response
        response = {
            'statusCode': 200,
            'body': json.dumps('User registered successfully!')
        }

    except ValueError as ve:
        # Handle missing or invalid 'body' in the request
        response = {
            'statusCode': 400,
            'body': json.dumps(f'Error: {str(ve)}')
        }

    except Exception as e:
        # Return an error response if something goes wrong
        response = {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

    return response
















































    # try:
    #     # Parse registration data from the Lambda event
    #     body = json.loads(event['body'])
    #     user_name = body['user_name']
    #     email = body['email']

    #     # Store data in DynamoDB
    #     table.put_item(
    #         Item={
    #             'user_name': user_name,
    #             'email': email
    #         }
    #     )

    #     # Return a successful response
    #     response = {
    #         'statusCode': 200,
    #         'body': json.dumps('User registered successfully!')
    #     }

    # except Exception as e:
    #     # Return an error response if something goes wrong
    #     response = {
    #         'statusCode': 500,
    #         'body': json.dumps(f'Error: {str(e)}')
    #     }

    # return response
