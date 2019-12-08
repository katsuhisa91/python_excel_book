import json

task_data = {
    'id': 1,
    'name': 'Homework',
    'deadline': '2020/09/01'
}

with open('sample.json', 'x', newline='') as f:
    f.write(json.dumps(task_data))
