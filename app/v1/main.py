from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/stocks/{ticker}")
def get_stock(ticker: str):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")
    return hist.reset_index().to_dict(orient='records')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
