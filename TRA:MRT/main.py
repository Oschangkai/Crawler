import requests
from bs4 import BeautifulSoup #整理html
# 抓圖
try:
    from urllib import urlretrieve
except ImportError:
    from urllib.request import urlretrieve
#import time

traURL = 'https://queryweb.tscc.com.tw/tra_web/default.aspx'
mrtURL = 'https://queryweb.tscc.com.tw/mrt_web/default.aspx'
traImg = 'https://queryweb.tscc.com.tw/tra_web/vimg.aspx'
mrtImg = 'https://queryweb.tscc.com.tw/mrt_web/vimg.aspx'
header = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}

s = requests.Session()
req = s.get(traURL, headers=header)
imgreq = s.get(traImg, headers=header)
print('進入狀態：', req.status_code, imgreq.status_code)

dom = BeautifulSoup(req.text, 'lxml')
__VIEWSTATE = dom.find(id="__VIEWSTATE")['value']
__VIEWSTATEGENERATOR = dom.find(id = "__VIEWSTATEGENERATOR")['value']
__EVENTVALIDATION = dom.find(id = "__EVENTVALIDATION")['value']

imgFile = 'pic.png'
urlretrieve(traImg, imgFile)
OCR = input('驗證碼：')

postData = {'__VIEWSTATE' : __VIEWSTATE, #Enter Page's View State
'__VIEWSTATEGENERATOR' : __VIEWSTATEGENERATOR,
'__EVENTVALIDATION' : __EVENTVALIDATION,
'ctl00$ContentPlaceHolder1$txtSDateS' : '02262016', #startDate--TRA:mmddYYYY,MRT:YYYYmmdd
'ctl00$ContentPlaceHolder1$txtSDateE' : '02272016', #endDate--TRA:mmddYYYY,MRT:YYYYmmdd
'ctl00$ContentPlaceHolder1$txtCardID' : '', #cardID
'ctl00$ContentPlaceHolder1$TextBox1': '', #birthday--mmdd
'ctl00$ContentPlaceHolder1$txtValidateCode': OCR, #ValidateCode
'ctl00$ContentPlaceHolder1$cmdQuery' : '查詢'
}


post = s.post(traURL, data = postData)
domP = BeautifulSoup(post.text, 'lxml')
result = domP.find_all(id="ctl00_ContentPlaceHolder1_lblResult")
print(result)
open('hi.html', 'w').write(domP.prettify())

