from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask on Render!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Render default port 10000 hai
    app.run(host='0.0.0.0', port=port)

from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Stock & Crypto Analysis API is running!"}

@app.get("/get-data/")
def get_stock_data(symbol: str, capital: float):
    stock = yf.Ticker(symbol)
    data = stock.history(period='1d')
    
    if data.empty:
        return {"error": "Invalid Stock/Crypto Symbol!"}

    last_price = data['Close'].iloc[-1]
    
    risk_percentage = 2 / 100  # 2% risk
    tp_percentage = 4 / 100  # 4% profit target
    
    sl = round(last_price - (last_price * risk_percentage), 2)
    tp = round(last_price + (last_price * tp_percentage), 2)

    return {
        "symbol": symbol.upper(),
        "last_price": round(last_price, 2),
        "stop_loss": sl,
        "take_profit": tp,
        "capital": capital
    }

