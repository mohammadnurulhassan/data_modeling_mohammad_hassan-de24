import json
from pathlib import Path
from connect_mongo import get_collection
from pymongo.errors import BulkWriteError, DuplicateKeyError

def read_json(json_file):
    with open(json_file, "r") as file:
        return json.load(file)
    
def insert_profiles_records(collection,data):
    collection.create_index("user_id", unique=True)
    collection.insert_many(data)
    collection.insert_many(data)
    

if __name__ == '__main__':
    profiles_path = Path(__file__).parent / "linkedin_profiles.json"

    profiles_data = read_json(profiles_path)

    profile_collection = get_collection("linkedin", "profile")

    try:
        insert_profiles_records(profile_collection, profiles_data)
    except (BulkWriteError, DuplicateKeyError) as err:
        print(err)
