import requests

for api_key in range(1,100,2):
    response = requests.get(f'<ip_addr>/api/{api_key}')
    print(f'Value:{response.json()}')


