from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bkcharts import Scatter, output_file, show, Horizon, Line, TimeSeries
import pandas as pd
from pandas_datareader import data, wb

# define start and end dates
start_date = '2016-06-26'
end_date = '2016-12-31'

# load data from sources
ford = data.DataReader("NYSE:F", "google", start_date, end_date)
generalmotors = data.DataReader("NYSE:GM", "google", start_date, end_date)
tesla = data.DataReader("TSLA", "google", start_date, end_date)

'''
Close Prices
'''
stocks = pd.DataFrame({
    "NYSE:F": ford["Close"],
    "TSLA": tesla["Close"],
    "NYSE:GM": generalmotors["Close"]})

stocks.head()
stocks.reset_index(inplace=True)

# p = Scatter(stocks, x='Date', y='TSLA', title='TSLA Close Price', xlabel = 'Date', ylabel='Close Price')

p = Line(stocks, x='Date')
output_file("close.html")

show(p)

'''
Volume, Change in Volume
'''

stock_volume = pd.DataFrame({
    "NYSE:F": ford["Volume"],
    "TSLA": tesla["Volume"],
    "NYSE:GM": generalmotors["Volume"]})

stock_volume.head()
stock_volume.reset_index(inplace=True)

# values for volumechange function

F_volume = stock_volume['NYSE:F'].tolist()
F_vol_change = []

TSLA_volume = stock_volume['TSLA'].tolist()
TSLA_vol_change = []

GM_volume = stock_volume['NYSE:GM'].tolist()
GM_vol_change = []


# creates list of volume changes

def volume_change(x, k):
    for i in range(0, ((len(x)) - 1)):
        hold = x[i + 1]
        diff = (hold - x[i])
        k.append(diff)
        i + 1
    return k


print(volume_change(F_volume, F_vol_change))
print(volume_change(TSLA_volume, TSLA_vol_change))
print(volume_change(GM_volume, GM_vol_change))

# correlation heat map .. createbetter
correlated = stocks.corr()

corrMatrix = correlated.as_matrix()

N = 3
factors = ['Tesla', 'Ford', 'GM']
x = []
y = []
colors = []
for i in range(N):
    for j in range(N):
        x.append(factors[j])
        y.append(factors[i])
        cor = corrMatrix[i, j]
        rgb = (int(abs(cor) * 255), 0, int((1 - abs(cor)) * 255))
        colors.append('#%02x%02x%02x' % rgb)

p2 = figure(x_range=factors, y_range=factors)

p2.rect(x, y, color=colors, width=1, height=1)
output_file("heatmap.html")
show(p2)


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

oil_dataframe = oil_prices_recent[(start_date < oil_prices_recent.index) & (oil_prices_recent.index < end_date)]








