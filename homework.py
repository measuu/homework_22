import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles
import pandas as pd
import time

#Завдання 1

data = {
    'TransactionID': [501, 502, 503, 504, 505],
    'TransactionDate': ['2023-12-01', '31/12/2023', 'December 15, 2023', '2023/12/20', '2023-13-01']
}

transactions_df = pd.DataFrame(data)
transactions_df['TransactionDate'] = pd.to_datetime(transactions_df['TransactionDate'],format='mixed', errors='coerce')
transactions_df['Year'] = transactions_df['TransactionDate'].dt.year
transactions_df['Month'] = transactions_df['TransactionDate'].dt.month
print(transactions_df)

#Завдання 2

timestamps_df = pd.DataFrame({
    'TimestampID': [601, 602, 603, 604],
    'UnixTimestamp': [1704067200, 1704153600, 1704240000, 1704326400]
})

timestamps_df['UnixTimestamp'] = pd.to_datetime(timestamps_df['UnixTimestamp'], unit='s', )
timestamps_df['Year'] = timestamps_df['UnixTimestamp'].dt.year
timestamps_df['Month'] = timestamps_df['UnixTimestamp'].dt.month
timestamps_df['Days'] = timestamps_df['UnixTimestamp'].dt.day
timestamps_df['Hours'] = timestamps_df['UnixTimestamp'].dt.hour

print(timestamps_df)

# #Завдання 3

dates_df = pd.DataFrame({
    'EntryID': [701, 702, 703, 704, 705],
    'DateString': ['2024-02-30', '02/28/2024', '2024/03/15', 'March 32, 2024', '2024-04-10']
})

dates_df['DateString'] = pd.to_datetime(dates_df['DateString'], format='%Y-%m-%d', errors='coerce')
print(dates_df)

#Завдання 4
