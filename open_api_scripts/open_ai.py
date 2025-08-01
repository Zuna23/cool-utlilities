import os
import openai
import boto3
ssm = boto3.client('ssm')
parameter = ssm.get_parameter(Name='/openai/api_key', WithDecryption=True)
openai.api_key = parameter['Parameter']['Value']
openai.Model.list()


print(openai.Model.list())