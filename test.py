import requests

password = "AIzaSyCzmABOfcTbibaP_VmZPsFn0q3Ro2sXlHQ"

response = requests.get('http://google.com', {'password': password})

print(response.json())
