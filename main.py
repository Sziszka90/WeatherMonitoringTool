# Weather API
import query_data
import process_data
import db
import time
from decouple import config

while(True):
    data, data_to_plot = query_data.query_from_api()
    process_data.create_file(data)
    process_data.create_plot(data_to_plot)
    db.save_to_db(data)
    print(data)

    time.sleep(int(config('TIME_REQUEST')))