import argparse
import boto3

# Initialize the AWS Lambda and CloudWatch Events clients
lambda_client = boto3.client('lambda')
events_client = boto3.client('events')

def enable_lambda_triggers(lambda_function_name):
    # Enable the triggers by updating the state of the associated CloudWatch Event Rules
    rules = events_client.list_rule_names_by_target(TargetArn=lambda_function_name)
    for rule in rules['RuleNames']:
        events_client.enable_rule(Name=rule)
        print(f"Enabled trigger: {rule}")

def disable_lambda_triggers(lambda_function_name):
    # Disable the triggers by updating the state of the associated CloudWatch Event Rules
    rules = events_client.list_rule_names_by_target(TargetArn=lambda_function_name)
    for rule in rules['RuleNames']:
        events_client.disable_rule(Name=rule)
        print(f"Disabled trigger: {rule}")

def main():
    parser = argparse.ArgumentParser(description="Enable or disable Lambda triggers")
    parser.add_argument("--function-name", required=True, help="Lambda function name")
    parser.add_argument("--action", required=True, choices=["enable", "disable"], help="Action to perform (enable or disable)")
    
    args = parser.parse_args()
    lambda_function_name = args.function_name

    if args.action == "enable":
        enable_lambda_triggers(lambda_function_name)
    elif args.action == "disable":
        disable_lambda_triggers(lambda_function_name)
    else:
        print("Invalid action. Use --enable or --disable.")

if __name__ == "__main__":
    main()
