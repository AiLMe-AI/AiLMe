import os
import json
import argparse
import requests


# Preprocess function
def preprocess_input(input_data):
    if os.path.isfile(input_data):
        print(f'Input is a file path: {input_data}')

        def data_generator():
            with open(input_data, 'r') as f:
                for line in f:
                    data = json.loads(line)
                    print(f'Read and parsed a line from the file: {data}')
                    yield data

        return data_generator()
    else:
        try:
            data = json.loads(input_data)
            print(f'Parsed command line argument: {data}')
            return iter([data])  # Wrap a single data into an iterator
        except json.JSONDecodeError:
            raise ValueError(f'Invalid input: {input_data}. Please provide a valid JSON string or file path.')


# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('input_data', help='Command line JSON argument or JSON file path')
parser.add_argument('--stream', action='store_true', help='Turn on stream mode for requests')
args = parser.parse_args()

# Call preprocess function to handle input
data_iter = preprocess_input(args.input_data)

# Initialize request parameters
url = 'https://model-api.ailme.ai/'
headers = {
    'X-Auth-Key': '<your-auth-token>',
    'Content-Type': 'application/json'
}

# Traverse all data and send requests
for data in data_iter:
    if args.stream:
        with requests.post(url + 'web/chat/stream', headers=headers, json=data, stream=True) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if line:
                    # json_line = json.loads(line)
                    print(f'New data from stream: {line}')
    else:
        response = requests.post(url + 'web/chat', headers=headers, json=data)
        print(f'Response content: {response.json()}')
