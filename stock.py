import pandas as pd
import datetime

import requests 
from bs4 import BeautifulSoup

def real_time_price(stock_code):
    url =('https://www.google.com/finance/quote/')+stock_code+(':NSE')
    r=requests.get(url)
    web_content = BeautifulSoup(r.text, 'lxml')
    web_content = web_content.find('div', class_="YMlKec fxKbKc").text
    
    if web_content ==[]:
        web_content = '99999'
        
    return (web_content)

NSE= ['ITC', 'rcf', 'RELIANCE', 'HDFCBANK','JUSTDIAL' ]


for step in range(1,1000000000000000000000001):
    price=[]
    col =[]
    time_stamp= datetime.datetime.now()
    time_stamp=time_stamp.strftime("%Y-%m-%d %H:%M:%S")
    for stock_code in NSE:
        price.append(real_time_price(stock_code))
        
    col = [time_stamp]
    col.extend(price)
    df = pd.DataFrame(col)
    df = df.T
    df.to_csv('realtimestock.csv', mode='a', header= False)
    print(col) 
 