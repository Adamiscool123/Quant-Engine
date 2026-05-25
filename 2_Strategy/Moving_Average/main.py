import pandas as pd

data_path = "/home/adamidrissi/Quant-Engine/1_Data/^GSPC.csv"

with open(data_path, "r") as f:
    data = f.read()