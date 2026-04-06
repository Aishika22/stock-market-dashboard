from flask import Flask, render_template, request
from stock_analysis import analyze_stock
from datetime import datetime
import os

app = Flask(__name__)

if not os.path.exists("static"):
    os.makedirs("static")


@app.route("/", methods=["GET", "POST"])
def index():
    plot = None
    price = high = low = trend = None
    stock_name = None
    today_date = datetime.now().strftime("%d %B %Y")

    if request.method == "POST":
        stock = request.form.get("stock")

        if stock:
            stock_name = stock.upper()
            plot, price, high, low, trend = analyze_stock(stock)

    return render_template(
        "index.html",
        plot=plot,
        price=price,
        high=high,
        low=low,
        trend=trend,
        stock_name=stock_name,
        today_date=today_date
    )


if __name__ == "__main__":
    app.run(debug=True)