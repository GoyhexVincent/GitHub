from matplotlib import pyplot as plt
import numpy as np
import urllib
from matplotlib import dates as mdates
import datetime as dt
from matplotlib import style

print(plt.style.available)
#style.use('ggplot')
style.use('fivethirtyeight')
def bytespdate2num(fmt, encoding = 'utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter
        

def graph_data(stock):

    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1),(0,0))
    
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)
    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,
                                                          # %Y = full year = 2015
                                                          # %y = partial year = 15
                                                          # %m = number month
                                                          # %d = number day
                                                          # %H = hours
                                                          # %M = minutes
                                                          # %S = seconds
                                                          converters={0: bytespdate2num('%Y%m%d')})
    with plt.xkcd():
        ax1.plot_date(date, closep, '-', label='price')
        ax1.plot([],[],linewidth=5, label='loss', color='r')
        ax1.plot([],[], linewidth=5, label='gain', color='g')
        ax1.fill_between(date, closep, closep[0],where=(closep > closep[0]),facecolor='g', alpha=0.3)
        ax1.fill_between(date, closep, closep[0],where=(closep < closep[0]),facecolor='r', alpha=0.3)
        
        
        for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45)
        ax1.grid(True,color='w',linestyle='-', linewidth=1.5)
        ax1.xaxis.label.set_color('black')
        ax1.yaxis.label.set_color('black')
        ax1.set_yticks([50,75,100])
            
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('BP Price evolution \n check it out!')
        plt.legend()
        plt.subplots_adjust(left=0.09,bottom=0.18,right=0.94,top=0.90,wspace=0.2,hspace=0)
        
        plt.show()
    
graph_data('BP')

