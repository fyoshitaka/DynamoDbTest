import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('hello')

def lambda_handler(event, context):

    table_name = "CARD_TABLE"
    dynamotable = dynamodb.Table(table_name)
'''　update sample
    primary_key =  {'CARD_NO': "123"}
    attr = {
                'balance':{
                    'Action': 'PUT',
                    'Value': "10000"
                }
            }

    res = dynamotable.update_item(Key=primary_key, AttributeUpdates=attr, ReturnValues='UPDATED_NEW')
'''
# read sample
    primary_key =  {'CARD_NO': "321"}
    res = dynamotable.get_item(Key=primary_key)

    return res
    