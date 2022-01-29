import pymongo
from decouple import config
from datetime import datetime

def save_to_db(data: dict) -> None:

    try:
        client = pymongo.MongoClient(host=config('DB_NAME'),
                                     username=config('DB_USER'),
                                     password=config('DB_PASSWORD'),
                                     port=int(config('DB_PORT')))

    except pymongo.errors.ConnectionFailure as e:
        raise SystemExit(e)


    db = client["Data"]

    collection = db["WeatherData"]

    data["_id"] = int(datetime.now().timestamp())

    collection.insert_one(data)