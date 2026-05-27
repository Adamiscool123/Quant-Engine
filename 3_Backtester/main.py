import pandas as pd

dataset_signals = r"C:\Users\adami\OneDrive\Documents\quant_engine\2_Strategy\Moving_Average\buy_sell_signals.csv"

dataset_stock = r"C:\Users\adami\OneDrive\Documents\quant_engine\1_Data\GSPC.csv"

column_names = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume', 'SMA_200']

df_signals = pd.read_csv(dataset_signals)

df_stock = pd.read_csv(dataset_stock, skiprows=3, names=column_names)

df_stock_cleaned = df_stock.dropna().copy()

stock_open = df_stock_cleaned["Open"]

stock_date = df_stock_cleaned["Date"]

signal_date = df_signals["Date"]

signal_close = df_signals["Close"]

current_cash = 1000

for i in range(0, len(stock_date)):
    if(stock_date.iloc[i] == signal_date.iloc[i]):
        current_open = stock_open.iloc[i]
        current_close = signal_close.iloc[i]

        percent_increase = 0

        if(current_close-current_open < 0):
            percent_increase = (current_open-current_close)/current_close

            current_cash = current_cash-(current_cash*percent_increase)
        else:
            percent_increase = (current_close-current_open)/current_close

            current_cash = current_cash+(current_cash*percent_increase)

print(current_cash)