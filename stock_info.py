import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf
import datetime as dt

start = dt.datetime(2000,1,1)
end = dt.datetime.now()
stock = input('Please enter the ticker symbol for the stock you wish to view: ')

def stock_to_csv(stock):
    stock = stock.upper()
    df = web.DataReader(name = stock, data_source='yahoo', start = start, end = end)
    df.to_csv(f'{stock}_stock_information_2010_to_2020.csv')


def plot_stock(stock):
    df = web.DataReader(name = stock, data_source='yahoo', start = start, end = end)
    #------ Restructure the data frame
    df2 = df[['Open','High','Low','Close']]
    mpf.plot(df2)
    plt.show()


stock_to_csv(stock)
plot_stock(stock)
    
