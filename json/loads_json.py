import json

with open('sample.json', 'r', newline='') as f:
    sample_data = json.loads(f.read())
    print(sample_data)
