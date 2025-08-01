import boto3

def list_lambdas_with_active_triggers():
    lambda_client = boto3.client('lambda')

    try:
        response = lambda_client.list_functions()
        functions = response['Functions']

        for function in functions:
            function_name = function['FunctionName']
            triggers = lambda_client.list_event_source_mappings(FunctionName=function_name)['EventSourceMappings']

            if triggers:
                print(f"Function: {function_name} has active triggers.")
    
    except Exception as e:
        print(f"Error listing Lambda functions: {e}")

def disable_active_triggers():
    lambda_client = boto3.client('lambda')

    try:
        response = lambda_client.list_functions()
        functions = response['Functions']

        for function in functions:
            function_name = function['FunctionName']
            triggers = lambda_client.list_event_source_mappings(FunctionName=function_name)['EventSourceMappings']

            for trigger in triggers:
                uuid = trigger['UUID']
                lambda_client.update_event_source_mapping(UUID=uuid, Enabled=False)
                print(f"Trigger {uuid} for function {function_name} has been disabled.")
    
    except Exception as e:
        print(f"Error disabling triggers: {e}")

if __name__ == "__main__":
    print("Listing functions with active triggers:")
    list_lambdas_with_active_triggers()

    print("\nDisabling active triggers:")
    disable_active_triggers()
