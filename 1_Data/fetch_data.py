import yfinance as yf

stock = "^GSPC"

data = yf.Ticker(stock)

df = yf.download(stock, period="10y")

df.to_csv(f"{stock}.csv")