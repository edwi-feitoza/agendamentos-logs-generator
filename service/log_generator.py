import uuid

class LogGenerator:
    def generate_log(self, http_method, http_status, latency, log_timestamp, log_request_time):
        log = {
            'timestamp': log_timestamp,
            'log_message': {
                'aws_account_id': '123456789012',
                'apigw': {
                    'endpoint_url': 'mainserver.edwifeitoza.com.br',
                    'apigw_id': '1234567890',
                    'stage': 'prod',
                    'context-path': '/v1/qualquerbosta',
                    'resource_id': 'wwwkkk',
                    'http_method': http_method,
                    'base_path_matched': '-'
                },
                'transaction': {
                    'request': {
                        'request_id': str(uuid.uuid4()),
                        'request_time': log_request_time,
                        'source_ip': '10.0.0.1',
                        'user_agent': 'Jersey/3.1.0 (Apache HttpClient 4.5.12)',
                        'tls_version': 'TLSv1.2',
                        'protocol': 'HTTP/1.1'
                    },
                    'response': {
                        'status': http_status['http_status_code'],
                        'error': http_status['error_code'],
                        'latency': latency

                    }
                },
                'tracing': {
                    'correlation_id': str(uuid.uuid4()),
                    'x-ray-trace': 'Root=1-{}'.format(str(uuid.uuid4()))
                },
                'network': {
                    'vpc_id': 'vpc-1234567890',
                    'vpce_id': 'vpce-1234567890',
                    'vpc_link': 'null'
                },
                'authorizer': {
                    'identity': {
                        'client_id': str(uuid.uuid4()),
                        'type': 'STS_ISS',
                        'app_id': 'ES2SUPERCARAIOAQUATRODAPORRATODALA',
                        'kid': '{}.prd.gen.1111111111111.jwt'.format(str(uuid.uuid4()))
                    },
                    'response': {
                        'status': '200',
                        'error': '-',
                        'latency': '284'
                    }
                },
                'integration': {
                    'response': {
                        'status': '200',
                        'error': '-',
                        'latency': '248'
                    }
                }
            }
        }
        return log
