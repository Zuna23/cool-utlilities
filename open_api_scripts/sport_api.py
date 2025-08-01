


import requests
import boto3

url = "https://rapidapi.com/api-sports/api/api-football"

querystring = {"id":"61"}

ssm = boto3.client('ssm')
rapidapi_key = ssm.get_parameter(Name='rapidapi', WithDecryption=True)['Parameter']['Value']

headers = {
	"X-RapidAPI-Key": rapidapi_key,
	"X-RapidAPI-Host": "api-football-beta.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response)
