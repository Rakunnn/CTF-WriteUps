import requests

for api_key in range(1,100,2):
    response = requests.get(f'http://10.10.67.14/api/{api_key}')
    print(f'Value:{response.json()}')


