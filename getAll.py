import boto3
import json
dynamo = boto3.client("dynamodb")

def handler(event, context):
	response = dynamo.query(
		TableName = "users",
		ExpressionAttributeValues={
			':v1': {
				'S': 'USER',
			},
		},
		KeyConditionExpression = "PK=:v1"
	)

	item = response.get("Items")

	return {
        "headers": {
            "Content-Type": "application/json",
        },
        "statusCode": 200,
        "body": json.dumps(item)
    }
