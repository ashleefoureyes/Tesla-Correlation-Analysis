import datetime as dt
import time
import pandas as pd
import pandas_datareader.data as web

# provides price per barrel

url = "https://www.quandl.com/api/v3/datasets/CHRIS/CME_CL1.csv"
oil_prices = pd.read_csv(url, index_col=0, parse_dates=True)
oil_prices.sort_index(inplace=True)
oil_prices_recent = oil_prices['Last']
oil_prices['PctCh'] = oil_prices.Last.pct_change()

