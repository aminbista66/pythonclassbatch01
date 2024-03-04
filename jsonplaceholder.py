import requests

api_url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(api_url)

import json


print(json.dumps(response.json(), indent=4))