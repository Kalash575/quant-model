import requests

def send_signal(msg):
    TOKEN = "7494189301:AAEjSatA69sp0FxJZCByesBR8nL-CQb9i_Y"
    CHAT_ID = "5601858231"
    url = f"https://api.telegram.org/bot{7494189301:AAEjSatA69sp0FxJZCByesBR8nL-CQb9i_Y}/sendMessage?chat_id={5601858231}&text={msg}"
    requests.get(url)
