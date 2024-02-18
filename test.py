import requests

password1 = "test"
password2 = "tomer123"

response = requests.get('http://google.com', {'password': password})

print(response.json())
