#Recieve message.py
import json
import boto3
from datetime import datetime

client = boto3.client('sqs')

def lambda_handler(event, context):
    # TODO implement
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Message received at ", current_time)
    print("=========================")
    response = client.receive_message(QueueUrl='https://sqs.us-east-1.amazonaws.com/661279896448/CaseTestQueue',MaxNumberOfMessages=10)
    print(response)
    print("=========================")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Pipeline Lambda!')
    }
