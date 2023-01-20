import json
import decimalencoder
import todoList

def translate(event, context):
    target_language = event['pathParameters']['language']
    id = event['pathParameters']['id']
    item = todoList.translate_item(id,
                                   target_language)
    if item:
        response = {
            "statusCode": 200,
            "body": json.dumps(item,
                               cls=decimalencoder.DecimalEncoder)
        }
    else:
        response = {
            "statusCode": 404,
            "body": ""
        }
    return response
