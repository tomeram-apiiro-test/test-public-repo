import requests

password = "#@vfdsd435trGSAFg"

response = requests.get('', {'password': password})

print(response.json())
