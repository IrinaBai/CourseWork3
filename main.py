from utils import executed_operations, newest_operations, load_json
import json
from datetime import datetime

def main():
    data = load_json()
    filtered_operations = executed_operations(data)
    newest_ops = newest_operations(filtered_operations)

    # Convert date format to ДД.ММ.ГГГГ
    for operation in newest_ops:
        date_str = operation.get('date')
        date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
        operation['date'] = date_obj.strftime('%d.%m.%Y')

    newest_ops_json = json.dumps(newest_ops, indent=2, ensure_ascii=False)
    print(newest_ops_json)



if __name__ == "__main__":
    main()
