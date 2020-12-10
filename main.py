# This is a sample Python script.
import requests
from bs4 import BeautifulSoup
import time
# import pandas as pd

# SUUMO 賃貸　東京都足立区　検索
url = 'https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ta=13&sc=13121&cb=0.0&ct=9999999&et=9999999&cn=9999999&mb=0&mt=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&fw2=&srch_navi=1'
#データ取得
result = requests.get(url)
c = result.content

#HTMLを元に、オブジェクトを作る
soup = BeautifulSoup(c, features="html.parser")

#物件リストの部分を切り出し
summary = soup.find("div", {'id': 'js-bukkenList'})

print(summary)

#ページ数を取得
body = soup.find("body")
pages = body.find_all("div",{'class':'pagination pagination_set-nav'})
pages_text = str(pages)
pages_split = pages_text.split('</a></li>\n</ol>')
pages_split0 = pages_split[0]
pages_split1 = pages_split0[-3:]
pages_split2 = pages_split1.replace('>','')
pages_split3 = int(pages_split2)

urls = []

#1ページ目を格納
urls.append(url)

#2ページ目から最後のページまでを格納
for i in range(pages_split3-1):
    pg = str(i+2)
    url_page = url + '&pn=' + pg
    urls.append(url_page)

urls