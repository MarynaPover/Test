import json

input_data = {100001: ('Jason', 75), 100002: ('Sarah', 22), 100003: ('Ben', 13), 100004: ('Paul', 26), 100005: ('Mino', 46), 100006: ('Lilly', 8)}

with open('data_file.json', 'w') as f:
    json.dump(input_data, f)
