from indicators import calculate_indicators
from strategies import apply_strategies
from utils.scoring import calculate_score
from utils.telegram import send_signal
from utils.adaptive import update_model
import yfinance as yf

def load_live_data(symbol):
    df = yf.download(tickers=symbol, period="5d", interval="1m")
    return df

if __name__ == "__main__":
    data = load_live_data("^NSEI")  # for Nifty 50
    data = calculate_indicators(data)
    strategy_flags = apply_strategies(data)
    total_score = calculate_score(strategy_flags)

    if total_score >= 18:
        send_signal("✅ BUY Signal Triggered")
    elif total_score <= -18:
        send_signal("❌ SELL Signal Triggered")

    update_model(strategy_flags, outcome="profit/loss")
