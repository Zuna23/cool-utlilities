import boto3

cloudwatch_client = boto3.client('events')
lambda_client = boto3.client('lambda')

def list_lambda_triggers(function_name):
    try:
        response = cloudwatch_client.list_rules(NamePrefix=f"Target-Lambda-{function_name}")
        rules = response['Rules']

        for rule in rules:
            targets = rule['Targets']
            for target in targets:
                if target['Arn'] == f"arn:aws:lambda:REGION:ACCOUNT_ID:function:{function_name}":
                    print(f"CloudWatch Event Rule: {rule['Name']} triggers Lambda function {function_name}")

    except Exception as e:
        print(f"Error listing Lambda triggers: {e}")

# Replace 'function_name' with the actual name of your Lambda function
list_lambda_triggers('function_name')
