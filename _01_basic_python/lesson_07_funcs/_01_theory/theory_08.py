import requests

url = "https://github.com/"
response = requests.get(url)
print(response.status_code)