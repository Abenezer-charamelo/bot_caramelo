import requests
import json
def send(to_,msg):
    url="https://api.telegram.org/bot910587910:AAH7vmMms6iG76kEpHUUDGASefUFoRGOXmQ/sendmessage?chat_id={}&text={}".format(to_,msg)
    requests.get(url)
def chat_id_extractor(js):
    cht_id=js["result"][0]["message"]["from"]["id"]
    return cht_id
"""token = "https://api.telegram.org/bot910587910:AAH7vmMms6iG76kEpHUUDGASefUFoRGOXmQ/getupdates?offset=246240940"
r=requests.get(token)
cus = json.loads(r.content)
print(chat_id_extractor(cus))"""

