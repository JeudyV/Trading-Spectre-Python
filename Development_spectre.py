import requests
import json

def Requesting_a_token():

    url = 'https://wss.hyper-api.com/token.php'

    payload = {
        "code":"a9ed8e9ace29e3f6ac08661712e0780eb51d4302",
        "grant_type":"authorization_code"
    }
    headers = {
          "Accept": "application/json",
          "Content-Type": "application/x-www-form-urlencoded",
          'Authorization': 'Basic YmM3OTVjNWQ1YTc2MzFlMGM1ZWI5YjdkZDU0NjJkZDE6NjgxMDE1NzE5ZDAyYmM0NDE2ZjE0YTg3ZjY2N2E1'
        }

    print(type(headers))
    print(type(payload))

    response = requests.request("POST", url, headers=headers, data = payload)

    print(response)

    print(response.text.encode('utf8'))
    #print(type(response))
    
    #result = json.dumps(response)

    #print(type(result))

    #result = response.json()
    

Requesting_a_token()