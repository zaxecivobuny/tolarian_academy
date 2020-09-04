import requests

url = "https://api.tcgplayer.com/app/authorize/authCode"

headers = {"accept": "application/json"}

response = requests.request("POST", url, headers=headers)

print(response.text)