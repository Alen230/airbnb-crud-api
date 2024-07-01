import json
import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('AirbnbListings')

def lambda_handler(event, context):
    http_method = event['httpMethod']
    
    if http_method == 'GET':
        return get_listing(event)
    elif http_method == 'POST':
        return create_listing(event)
    elif http_method == 'PUT':
        return update_listing(event)
    elif http_method == 'DELETE':
        return delete_listing(event)
    else:
        return {
            'statusCode': 405,
            'body': json.dumps('Method Not Allowed')
        }

def get_listing(event):
    listing_id = event['queryStringParameters']['id']
    try:
        response = table.get_item(Key={'id': listing_id})
        
        if 'Item' in response:
            return {
                'statusCode': 200,
                'body': json.dumps(response['Item'], cls=DecimalEncoder)
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps('Listing not found')
            }
    except Exception as e:
        print(f"Error fetching listing: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error fetching listing: {str(e)}")
        }

def create_listing(event):
    data = json.loads(event['body'], parse_float=Decimal)
    table.put_item(Item=data)
    return {
        'statusCode': 201,
        'body': json.dumps('Listing created successfully')
    }

def update_listing(event):
    listing_id = event['queryStringParameters']['id']
    data = json.loads(event['body'], parse_float=Decimal)
    
    update_expression = "set "
    expression_attribute_values = {}
    for key, value in data.items():
        update_expression += f"{key} = :{key}, "
        expression_attribute_values[f":{key}"] = value
    update_expression = update_expression.rstrip(", ")
    
    response = table.update_item(
        Key={'id': listing_id},
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_attribute_values,
        ReturnValues="UPDATED_NEW"
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Listing updated successfully')
    }

def delete_listing(event):
    listing_id = event['queryStringParameters']['id']
    table.delete_item(Key={'id': listing_id})
    return {
        'statusCode': 200,
        'body': json.dumps('Listing deleted successfully')
    }

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)
