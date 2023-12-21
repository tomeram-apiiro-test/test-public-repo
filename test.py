import requests

password1 = "AIzaSyCzmABOfcTbibaP_VmZPsFn0q3Ro2sXlHQ"
password2 = "tomer123"

response = requests.get('http://google.com', {'password': password})

print(response.json())
