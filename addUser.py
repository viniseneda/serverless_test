import boto3
import json

dynamo = boto3.client("dynamodb")

def handler(event, context):
	body = json.loads(event["body"])
	username = body.get("username")
	age = body.get("age")
	password = body.get("password")
	dynamo.put_item(
		TableName = "users",
		Item = {
			"PK": {
				"S": "USER"
			},
			"NAME": {
				"S": username
			},
			"password": {
				"S": password
			},
			"age": {
				"N": str(age)
			}
		}
	)

	return {
        "headers": {
            "Content-Type": "application/json",
        },
        "statusCode": 200,
        "body": "OK"
    }
