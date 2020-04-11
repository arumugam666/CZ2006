import requests

url = "https://us-central1-cz2006-9cd2d.cloudfunctions.net/app/addUser"

payload = "{\r\n\t\"userName\":\"Aru2\",\r\n\t\"passwordHash\":\"6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b\",\r\n\t\"loginEmail\": \"body.loginEmail\",\r\n\t\"updateEmail\": \"body.updateEmail\",\r\n\t\"updateFrequency\": \"1\",\r\n\t\"updateConfidence\": \"88\",\r\n\t\"watchList\": \"body.watchList\"\r\n}"
headers = {
  'Content-Type': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
