import requests

def send_signal(msg):
    TOKEN = "7494189301:AAEjSatA69sp0FxJZCByesBR8nL-CQb9i_Y"
    CHAT_ID = "5601858231"
    url = f"https://api.telegram.org/bot{7494189301:AAEjSatA69sp0FxJZCByesBR8nL-CQb9i_Y}/sendMessage?chat_id={5601858231}&text={msg}"
    requests.get(url)

# Check current IST time
def is_market_closed():
    ist = pytz.timezone('Asia/Kolkata')
    now = datetime.now(ist).time()
    market_close_time = time(15, 30)  # 3:30 PM IST
    return now >= market_close_time


# Send goodbye message
def send_goodbye_message():
    message = "📉 Market band hogaya bhai, kal milte hai 🚪 — Goobye Trader"
    url = f"https://api.telegram.org/bot{7494189301:AAEjSatA69sp0FxJZCByesBR8nL-CQb9i_Y}/sendMessage"
    payload = {
        'chat_id': 5601858231,
        'text': message,
        'parse_mode': 'Markdown'
    }
    requests.post(url, data=payload)

# Run check and send
if is_market_closed():
    send_goodbye_message()
