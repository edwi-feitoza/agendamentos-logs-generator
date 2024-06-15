import json
from datetime import datetime

class JsonGenerator:
    def create_json_log_file(self, content):
        file_suffix = datetime.now().isoformat()
        with open('logs/{}.json'.format(file_suffix), 'w') as log_file:
            final_content = json.dumps(content)
            log_file.write(final_content)
        print('File created successfully')
