#%%
import requests
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import dateutil.relativedelta
import pandas_datareader.data as web

dt = datetime.today()  
startdt = dt - dateutil.relativedelta.relativedelta(months=3)
seconds = str(int(dt.timestamp()))
startseconds = str(int(startdt.timestamp()))
print(startseconds)


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

# 網址
url = "https://query1.finance.yahoo.com/v8/finance/chart/2330.TW?period1="+startseconds+"&period2="+seconds+"&interval=1d&events=history&=hP2rOschxO0"

# 利用 requests 來跟遠端 server 索取資料
response = requests.get(url=url,headers=headers)

data = json.loads(response.text)
df = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0], index=pd.to_datetime(np.array(data['chart']['result'][0]['timestamp'])*1000*1000*1000))

df.close.plot()

#plt.show()

# set start and end dates 
start = datetime(2018, 2, 1) 
end = datetime(2020, 2, 1) 
# extract the closing price data
ultratech_df = web.DataReader(['2330.TW'], 'yahoo', start = start, end = end)['Close']
ultratech_df.columns = {'Close Price'}
ultratech_df.head(10)
