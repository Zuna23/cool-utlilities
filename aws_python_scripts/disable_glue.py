job_name = 'your_job_name'

response = glue_client.update_job(
    JobName=job_name,
    JobUpdate={
        'Triggers': [],  # This empty list disables triggers
    }
)

print(f"Trigger for job '{job_name}' disabled.")
