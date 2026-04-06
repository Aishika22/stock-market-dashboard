import yfinance as yf
import matplotlib.pyplot as plt


def analyze_stock(stock_input):
    stocks = stock_input.split(",")

    plt.figure(figsize=(12, 6))

    price = high = low = None
    trend = ""

    for stock in stocks:
        stock = stock.strip().upper()

        data = yf.download(stock, start="2022-01-01", end="2024-01-01")

        if data.empty:
            continue

        # Moving averages
        data['MA20'] = data['Close'].rolling(20).mean()
        data['MA50'] = data['Close'].rolling(50).mean()

        # Plot graph
        plt.plot(data['Close'], label=f"{stock} Close")
        plt.plot(data['MA20'], linestyle='--', label=f"{stock} MA20")

        # FIXED METRICS (NO ERROR NOW)
        if price is None:
            first_price = float(data['Close'].iloc[0])
            last_price = float(data['Close'].iloc[-1])

            price = round(last_price, 2)
            high = round(float(data['High'].max()), 2)
            low = round(float(data['Low'].min()), 2)

            trend = "UPTREND 📈" if last_price > first_price else "DOWNTREND 📉"

    plt.title("Stock Market Analysis")
    plt.legend()

    plot_path = "static/plot.png"
    plt.savefig(plot_path)
    plt.close()

    return plot_path, price, high, low, trend