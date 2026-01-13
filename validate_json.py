import json
import sys

try:
    with open('projects.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print("JSON is valid.")
    print(f"Number of items: {len(data)}")
    if len(data) > 0:
        print(f"Keys in first item: {list(data[0].keys())}")
except json.JSONDecodeError as e:
    print(f"JSON Decode Error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
