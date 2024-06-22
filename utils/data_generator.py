import random
from datetime import datetime, timedelta

class DataGenerator:
    def __init__(self, amount_data):
        self.__amount_data = amount_data
    def get_http_method(self):
        http_methods = ['GET', 'POST']
        weights = [0.8, 0.2]
        return random.choices(
            population=http_methods,
            weights=weights,
            k=self.__amount_data
        )

    def get_latency_description(self):
        latency_list = ['LOW', 'MEDIUM', 'HIGH']
        weights = [0.76, 0.22, 0.02]
        return random.choices(
            population=latency_list,
            weights=weights,
            k=self.__amount_data
        )

    def get_latency_time(self, description):
        if description == 'LOW':
            return str(random.choice([50, 350]))
        elif description == 'MEDIUM':
            return str(random.choice([351, 990]))
        elif description == 'HIGH':
            return str(random.choice([991, 2500]))

    def get_http_status_code(self):
        http_codes = [
            {'http_status_code': '206', 'error_code': '-'},
            {'http_status_code': '503', 'error_code': 'Service Unavailable'}
        ]
        weights = [0.986, 0.014]
        return random.choices(
            population=http_codes,
            weights=weights,
            k=self.__amount_data
        )

    def get_timestamps(self):
        list_dates = []
        start_time = datetime.now()
        end_time = start_time + timedelta(minutes=10)
        for i in range(0, self.__amount_data - 1):
            random_datetime = start_time + (end_time - start_time) * random.random()
            list_dates.append(random_datetime)
        list_dates.sort()
        return list_dates

    def get_formatted_timestamp(self, log_datetime):
        return log_datetime.isoformat(timespec='milliseconds')

    def get_formatted_request_time(self, log_request_time):
        date_format = '%d/%b/%Y:%H:%M:%S %z'
        return log_request_time.strftime(date_format)





