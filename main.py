# Weather API
import query_data
import process_data


data, data_to_plot = query_data.query_from_api()
process_data.create_file(data)
process_data.create_plot(data_to_plot)
print(data)


