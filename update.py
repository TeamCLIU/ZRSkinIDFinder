import json
import requests

URL = 'https://zombsroyale.io/api/shop/available'
request = requests.get(url=URL)
response = request.json()

if response['status'] == "success":
    print('Script executed successfully.')
else:
    print('Something went wrong.')

file = open("items.json", "w")
file.write(json.dumps(response))
file.close()