import requests
import json
import urllib3
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def load_json():
    url = 'https://jsonkeeper.com/b/5KVC'
    response = requests.get(url, verify=False)
    json_data = response.json()
    return json_data

def executed_operations(operations):
    executed_operations = []
    for operation in operations:
        if operation.get('state') == 'EXECUTED':
            executed_operations.append(operation)
    return executed_operations

def newest_operations(executed_operations):
    return list(sorted(executed_operations, key=lambda operation: datetime.strptime(operation.get('date'), '%Y-%m-%dT%H:%M:%S.%f'), reverse=True))[:5]

data = load_json()
filtered_operations = executed_operations(data)
newest_ops = newest_operations(filtered_operations)

newest_ops_json = json.dumps(newest_ops)
print(newest_ops_json)
