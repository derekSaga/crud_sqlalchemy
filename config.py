import json

with open("credentials.json") as json_file:
    data = json.load(json_file)

    USER = data['user']
    PASSWORD = data['password']
    HOST = data['host']
    SCHEMA = data['schema']
    DRIVER = data['driver']
    DIALECT = data['dialect']
    PORT = data['port']
