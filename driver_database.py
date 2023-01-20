"""
use json file as database
"""
import json 


async def get_data():
    with open("database.json") as f:
        return json.load(f)


async def write_data(data: dict):
    with open("database.json", "w") as fw:
        return json.dump(data, fw) 
           