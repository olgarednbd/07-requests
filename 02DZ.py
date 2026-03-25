import requests
import pprint

params = {
    "userId" : "1"
}

respons = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)

respons_json = respons.json()
pprint.pprint(respons_json)