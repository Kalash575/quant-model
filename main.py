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
