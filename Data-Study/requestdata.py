import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from dotenv import load_dotenv
import os


load_dotenv()
matplotlib.rc('font', family='AppleGothic')
matplotlib.rcParams['axes.unicode_minus'] = False

url = os.getenv("APIUrl")
Svkey=os.getenv("serviceKey")
print("url:", url)
print("serviceKey:", Svkey)
alldata=[]

for year in range(2012,2023):
    params ={'serviceKey' : Svkey, 'pageNo' : '1', 'numOfRows' : '10', 'cond[year::EQ]' : '{}'.format(year) }
    response = requests.get(url, params=params)
    data = json.loads(response.content)
    items = data['response']['body']['items']['item'][0]
    items['year']=year
    alldata.append(items)

df = pd.DataFrame(alldata)
df['total']=df['gnrl_f_cnt']+df['gnrl_m_cnt']
plt.bar(df['year'], df['total']/1e6)
plt.title('연도별 일반 여권 보유자 수')
plt.ylabel('단위 : 백만명')
plt.show()  