import subprocess
import re

# Run Terraform plan command and capture output
terraform_plan = subprocess.run(["terraform", "plan", "-out=tfplan"], capture_output=True, text=True)

# Capture the plan output
plan_output = terraform_plan.stdout

# Initialize dictionaries to store categorized resources
replace_resources = {}
create_resources = {}
update_resources = {}
destroy_resources = {}

# Define regular expressions to match different actions in the plan output
create_pattern = re.compile(r"\+ create (.+)")
replace_pattern = re.compile(r"\+/- replace (.+)")
update_pattern = re.compile(r"~ update in-place (.+)")
delete_pattern = re.compile(r"- destroy (.+)")

# Iterate through each line in the plan output
for line in plan_output.splitlines():
    create_match = create_pattern.search(line)
    replace_match = replace_pattern.search(line)
    update_match = update_pattern.search(line)
    delete_match = delete_pattern.search(line)

    if create_match:
        resource_name = create_match.group(1)
        create_resources.setdefault(resource_name, []).append(resource_name)
    elif replace_match:
        resource_name = replace_match.group(1)
        replace_resources.setdefault(resource_name, []).append(resource_name)
    elif update_match:
        resource_name = update_match.group(1)
        update_resources.setdefault(resource_name, []).append(resource_name)
    elif delete_match:
        resource_name = delete_match.group(1)
        destroy_resources.setdefault(resource_name, []).append(resource_name)

# Print categorized resources
print("Resources to be Created:")
for resource_name in create_resources:
    print(resource_name)

print("\nResources to be Replaced:")
for resource_name in replace_resources:
    print(resource_name)

print("\nResources to be Updated:")
for resource_name in update_resources:
    print(resource_name)

print("\nResources to be Destroyed:")
for resource_name in destroy_resources:
    print(resource_name)
