import requests


login = 'admin'
pas = 'admin'
url = f'https://secure-harbor-01729.herokuapp.com/api/v1/check_user/?format=json&user_login={login}&user_password={pas}'
response = requests.get(url)
print(response.status_code)
user_data = response.content
print(response.json())

