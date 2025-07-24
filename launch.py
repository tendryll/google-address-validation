import os
import requests

if __name__ == "__main__":
    api_key = os.environ.get("API_KEY")
    params = {'key': api_key}
    payload = {
      "address": {
        "regionCode": "US",
        "locality": "Mountain View",
        "addressLines": ["1600 Amphitheatre Pkwy"]
      }
    }
    r = requests.post(f'https://addressvalidation.googleapis.com/v1:validateAddress', params=params, json=payload)
    content = r.json()
    print(content)

