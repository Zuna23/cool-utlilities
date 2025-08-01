function_name = 'your_lambda_function_name'

response = lambda_client.list_event_source_mappings(
    FunctionName=function_name,
)

event_source_mappings = response['EventSourceMappings']


for mapping in event_source_mappings:
    mapping_uuid = mapping['UUID']

    # Disable the event source mapping
    lambda_client.update_event_source_mapping(
        UUID=mapping_uuid,
        FunctionName=function_name,
        Enabled=False
    )

    print(f"Disabled trigger with UUID {mapping_uuid}")
