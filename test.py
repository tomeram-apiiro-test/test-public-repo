import requests

password = "ghp_12345678901234567890123456789012"

response = requests.get('http://google.com', {'password': password})

print(response.json())
