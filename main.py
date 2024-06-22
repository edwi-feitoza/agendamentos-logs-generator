from service.log_generator import LogGenerator
from service.json_generator import JsonGenerator
from utils.data_generator import DataGenerator
from datetime import datetime

if __name__ == '__main__':
    log_generator = LogGenerator()
    json_generator = JsonGenerator()
    data_generator = DataGenerator(150_000)
    logs = []
    http_methods = data_generator.get_http_method()
    latency_description = data_generator.get_latency_description()
    status_code = data_generator.get_http_status_code()
    random_timestamps = data_generator.get_timestamps()
    for item in range(0, 149999):
        log_timestamp = data_generator.get_formatted_timestamp(random_timestamps[item])
        log_request_time = data_generator.get_formatted_request_time(random_timestamps[item])
        latency_time = data_generator.get_latency_time(latency_description[item])
        log = log_generator.generate_log(http_methods[item], status_code[item], latency_time, log_timestamp, log_request_time)
        logs.append(log)
    json_generator.create_json_log_file(logs)


