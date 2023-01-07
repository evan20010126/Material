import json

myObj = {'evan': 126, 'yumi': 531}

json_context = json.dumps(myObj, indent=4)

with open('write_json_file_result.json', 'w', encoding='utf-8') as f:
    f.write(json_context)
