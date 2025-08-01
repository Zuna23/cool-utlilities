import boto3
import argparse

# Initialize the AWS Glue client
glue_client = boto3.client('glue')

def list_glue_job_names():
    response = glue_client.get_jobs()
    job_names = [job['Name'] for job in response['Jobs']]
    return job_names

def get_trigger_names_by_job_name(job_name):
    # Get all Glue triggers
    all_triggers = glue_client.get_triggers()
    
    # Filter the triggers to find the ones associated with the specified job name
    job_triggers = [trigger['Name'] for trigger in all_triggers['Triggers'] if trigger['Actions'][0]['CrawlerName'] == job_name]
    
    return job_triggers

def disable_glue_triggers(job_name):
    # Get the triggers for the specified Glue job
    triggers = glue_client.get_triggers(JobName=job_name)
    
    # Disable each trigger
    for trigger in triggers['Triggers']:
        trigger_name = trigger['Name']
        glue_client.update_trigger(Name=trigger_name, Actions=[], Description="Trigger disabled")

def enable_glue_trigger(trigger_name, job_name, enabled=True):
    # Get the trigger's current configuration
    trigger = glue_client.get_trigger(Name=trigger_name)

    # Enable or disable the trigger based on the 'enabled' parameter
    trigger['Trigger']['Actions'][0]['CrawlerName'] = job_name
    trigger['Trigger']['Enabled'] = enabled

    # Update the trigger
    glue_client.update_trigger(Name=trigger_name, TriggerUpdate=trigger['Trigger'])



def main():
    parser = argparse.ArgumentParser(description="Enable or disable glue triggers")
    parser.add_argument("--action", required=True, choices=["enable", "disable"], help="Action to perform (enable or disable)")
    
    args = parser.parse_args()

    job_names = list_glue_job_names()
    for names in job_names:

    

        if args.action == "enable":
            enable_glue_trigger(get_trigger_names_by_job_name(names),names)
        elif args.action == "disable":
            disable_glue_triggers(names)
        else:
            print("Invalid action. Use --enable or --disable.")

if __name__ == "__main__":
    main()
