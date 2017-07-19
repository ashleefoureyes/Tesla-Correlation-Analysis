import datetime as dt
import time
import pandas as pd
import pandas_datareader.data as web

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
prices = []

dataFrame = pd.DataFrame(df)
print(dataFrame)
