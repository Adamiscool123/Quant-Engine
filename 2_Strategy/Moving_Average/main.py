import pandas as pd

data_path = "/home/adamidrissi/Quant-Engine/1_Data/^GSPC.csv"

df = pd.read_csv(data_path)

df_cleaned = df.dropna()

moving_average = df_cleaned['SMA_200']

close_price = df_cleaned['Close']

date = df_cleaned['Date']

print(moving_average)