import requests

def send_signal(msg):
    TOKEN = "your_bot_token"
    CHAT_ID = "your_chat_id"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}"
    requests.get(url)