from flask import Flask, flash, redirect, render_template, request, session
import yfinance as yf
msft = yf.Ticker("daslads")

app = Flask(__name__)
app.run(debug=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=="POST":
        ticker = request.form["ticker"].upper()
        try:
            stock = yf.Ticker(ticker)
            price = stock.info['currentPrice']
        except:
            return "ERROR: Not real ticker."
        return render_template('index.html', ticker=ticker, price=price)
    else:
        return render_template('index.html')