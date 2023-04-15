import json


def save_data(path_to_save, data):
    with open(path_to_save, "w") as f:
        data_str = json.dumps(data, indent=4)
        f.write(data_str)
