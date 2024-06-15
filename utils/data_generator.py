import random


class DataGenerator:
    def get_http_method(self):
        http_methods = ['GET', 'POST']
        weights = [0.8, 0.2]
        return random.choices(
            population=http_methods,
            weights=weights,
            k=20000
        )

    def get_latency_description(self):
        latency_list = ['LOW', 'MEDIUM', 'HIGH']
        weights = [0.76, 0.22, 0.02]
        return random.choices(
            population=latency_list,
            weights=weights,
            k=20000
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
            k=20000
        )

