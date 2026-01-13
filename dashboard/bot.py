import requests

token = "7876482640:AAE18GL12lbtPs2rHtge_o3J38WfTgyBRSA"
chat_id = "6752780496"

def telegram_send_mesage(text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    r = requests.post(url, data={"chat_id": chat_id, "text": text})
    return r.json()