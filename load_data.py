import datetime as dt
import time
import pandas as pd
import pandas_datareader.data as web
import bokeh


'''
Tesla Stock Information Load
'''

#set keys
tsla_open = 'Open'
tsla_high = 'High'
tsla_low = 'Low'
tsla_close = 'Close'
tsla_volume = 'Volume'

#setting start date, end date as today's date
start = dt.datetime(2015, 1, 1)
end = time.strftime("%x")

#load data from google finance

df = web.DataReader('TSLA', 'google', start, end)


#load dates from Tesla Data
dates = []
for i in range (len(df)):
    date_i = str(df.index[i])
    date_i = date_i[0:10]
    dates.append(date_i)


df['dates'] = dates



dataFrame = pd.DataFrame(df)

'''
oil prices
'''

#price per barrel

url = "https://www.quandl.com/api/v3/datasets/CHRIS/CME_CL1.csv"
oil_prices = pd.read_csv(url, index_col=0, parse_dates=True, )
oil_prices.sort_index(inplace=True)
oil_prices_recent = oil_prices['Last']
oil_prices['PctCh'] = oil_prices.Last.pct_change()

#set date range

oil_dataframe = oil_prices_recent[(start < oil_prices_recent.index) & (oil_prices_recent.index < end)]








