import pandas as pd

data_path = "/home/adamidrissi/Quant-Engine/1_Data/^GSPC.csv"

# 1. Skip the broken header rows (rows 0, 1, 2) and name them explicitly
column_names = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume', 'SMA_200']
df = pd.read_csv(data_path, skiprows=3, names=column_names)

# 2. Clean up any empty rows
df_cleaned = df.dropna(subset=['Close', 'SMA_200'])

# 3. Extract your columns safely
moving_average = df_cleaned['SMA_200']
close_price = df_cleaned['Close']
date = df_cleaned['Date']

buy = 0

sell = 0

# 4. Run your signal check
for i in range(-1, len(close_price)):
    if close_price.iloc[i] > moving_average.iloc[i]:
        buy+=1
    else:
        sell+=1

with open("sell_signals.txt", "w") as f:
    f.write(f"Sell signals: {sell}\n")