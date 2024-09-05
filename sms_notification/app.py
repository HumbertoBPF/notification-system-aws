import json
import os

import boto3


client = boto3.client('sns')
TopicArn = os.getenv("TopicArn")


def lambda_handler(event, context):
    records = event.get("Records", [])

    for record in records:
        event_body = json.loads(record["body"])

        client.publish(
            TopicArn=TopicArn,
            Message=event_body["message"],
            Subject=event_body["subject"],
        )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "success",
        }),
    }
