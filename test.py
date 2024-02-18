import requests

password1 = "test"
password2 = "tomer123"
password = "AIzaSyCzmABOfcTbibaP_VmZPsFn0q3Ro2sXlHQ"

response = requests.get('http://google.com', {'password': password})

print(response.json())
