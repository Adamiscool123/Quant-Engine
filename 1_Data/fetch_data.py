import yfinance as yf

stock = "^GSPC"

data = yf.Ticker(stock)

df = yf.download(stock, period="10y")

df['SMA_200'] = df['Close'].rolling(window=200).mean()

df.to_csv(f"{stock}_Moving_Averages.csv")