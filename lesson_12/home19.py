import json

input_data = {000001: ('Jason', 75), 000002: ('Sarah', 22), 000003: ('Ben', 13), 000004: ('Paul', 26), 000005: ('Mino', 46), 000006: ('Lilly', 8)}

with open('data_file.json', 'w') as f:
    json.dump(input_data, f)
