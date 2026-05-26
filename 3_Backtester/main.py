import pandas as pd

dataset_signals = "C:\Users\adami\OneDrive\Documents\quant_engine\2_Strategy\Moving_Average\buy_sell_signals.csv"

dataset_stock = "C:\Users\adami\OneDrive\Documents\quant_engine\1_Data\GSPC.csv"

df_signals = pd.read_csv(dataset_signals)

df_stock = pd.read_csv(dataset_stock)

