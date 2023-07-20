from utils import executed_operations, newest_operations, load_json
import json
def main():
    data = load_json()
    filtered_operations = executed_operations(data)
    newest_ops = newest_operations(filtered_operations)

    newest_ops_json = json.dumps(newest_ops, indent=2)
    print(newest_ops_json)

if __name__ == "__main__":
    main()
