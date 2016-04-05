#from distutils.core import setup
#import py2exe
import requests
from bs4 import BeautifulSoup
def dormQuery():
    dorm_url = 'https://portal.yzu.edu.tw/DomApply/DomApply_Ranking.aspx?AID=22&IfRecurrence=0&TypeNo=0&DomActionName=1051學年住宿申請'
    s = requests.Session()
    dorm_page = s.get(dorm_url)
    if dorm_page.status_code == 200:
        print('\n成功登入床位查詢頁面')
    else:
        print('\n床位查詢頁面登入失敗')

    dom = BeautifulSoup(dorm_page.text, 'lxml')
    boys = dom.find(id="ctl00_ContentPlaceHolder_MainEdit_GridView_ApplyerforActionM").text
    girls = dom.find(id="ctl00_ContentPlaceHolder_MainEdit_GridView_ApplyerforActionF").text
    
    file = open('boys.txt','w')
    boys = boys.replace('\n', '').replace('暫時排名性別籤號備註','').replace(' ','\n').replace('男', ' ')
    file.write(boys)

    file = open('girls.txt', 'w')
    girls = girls.replace('\n', '').replace('暫時排名性別籤號備註','').replace(' ','\n').replace('女', ' ')
    file.write(girls)

def findNo(num, gender):
    array = []
    with open(gender + '.txt') as line:
        for people in line:
            array.append(people)
    i = 0
    for item in array:
        if(item.endswith(num+'\n')):
            print(array[i])
            break
        i += 1

def ticket(num, gender):
    array = []
    with open(gender + '.txt') as line:
        for people in line:
            array.append(people)
    i = 0
    for item in array:
        if(item.startswith(num)):
            print(array[i])
            break
        i += 1

def findNoask(gender):
    num = input('請輸入籤號，離開請輸入exit：')
    while not num == 'exit':
        findNo(num, gender)
        num = input('請輸入籤號，離開請輸入exit：')

def ticketAsk(gender):
    num = input('請輸入排名，離開請輸入exit：')
    while not num == 'exit':
        ticket(num, gender)
        num = input('請輸入排名，離開請輸入exit：')

if __name__ == "__main__":
    print('(男)宿舍抽籤查詢')
    print('若停留此畫面太久，代表網路狀況不穩定')
    dormQuery()
    choose = input('1. 男宿, 2. 女宿  ')
    while not choose == '3':
        if choose == '1':
            gender = 'boys'
            break
        elif choose == '2':
            gender = 'girls'
            break
        else:  choose = input('\n輸入錯誤，請重新輸入！\n1. 男宿, 2. 女宿, 3. 離開  ')
    choose = input('\n1. 查籤號排名, 2. 查排名籤號, 3. 離開  ')
    while not choose == '3':
        if choose == '1':
            findNoask(gender)
            break
        elif choose == '2':
            ticketAsk(gender)
            break
        elif choose == '3':
            break
        else:  choose = input('\n輸入錯誤，請重新輸入！\n1. 查排名, 2. 查序號, 3. 離開  ')


#setup(
#    options = {'py2exe': {
#        'bundle_files': 1,
#        'compressed': True,
#    }},
#    console = [{'script': 'Hello.py',"icon_resources": [(1, "YZU_logo.ico")]}],
#    zipfile = None
#)