from indicators import calculate_indicators
from strategies import apply_strategies
from utils.scoring import calculate_score
from utils.telegram import send_signal
from utils.adaptive import update_model
import yfinance as yf

def load_live_data(symbol):
    df = yf.download(tickers=symbol, period="5d", interval="1m")
    return df
    
import time

while True:
    try:
        # Your model code here
        data = load_live_data("^NSEI")
        data = calculate_indicators(data)
        flags = apply_strategies(data)
        score = calculate_score(flags)

        if score >= 18:
            send_signal("✅ BUY Signal")
        elif score <= -18:
            send_signal("🔻 SELL Signal")

        update_model(flags, outcome="profit/loss")
    except Exception as e:
        print("⚠️ Error:", e)

    time.sleep(300)  # Wait 5 minutes before next run

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
