import requests
import json
from pprint import pprint as pprint

response = requests.get("https://api.github.com/users/zellwk/repos?type=owner&sort=updated")

todos = json.loads(response.text)

print(type(todos))
print(todos)

for tasks in todos:
    if tasks["owner"]["site_admin"] == False:
        pprint(tasks["id"])




