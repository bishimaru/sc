from django.core.management import BaseCommand
import csv
import urllib
from urllib import request
from bs4 import BeautifulSoup
import ssl
import datetime
import pandas as pd
import io,sys
from ... models import Data, TotalPay

ssl._create_default_https_context = ssl._create_unverified_context


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Hello World!')

        # まいジャグラー 
    url = 'https://p-ken.jp/p-charakawa/bonus/lot?ps_div=2&cost=21.28&model_nm=%CF%B2%BC%DE%AC%B8%DE%D7%B0III&day=1&mode='
    response = request.urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')
    find = soup.findAll('table')
    find = soup.findAll(id='dataTable')
    find = soup.findAll('td')

    list = []
    for row in find:
        row = row.text
        list.append(row)

    
    new_list = []
    for i in list[9:48]:
        num = i.replace('\r\n', '')
        num = num.replace("  ", "")
        new_list.append(num)

    
    mylist = [item for item in new_list if item != '']
    length = len(mylist)
    n=0
    s=4
    mm_list = []
    for i in mylist:
        mm_list.append(mylist[n:n+s:1])
        n += s
        if n >= length:
            break
    total = 0
    now = datetime.datetime.now()
    yesterday = now - datetime.timedelta(days=int(scrape_day))
    for i in mm_list:
        num = i[0]
        bb = i[1]
        rg = i[2]
        cnt = i[3]
        num = int(num)
        bb = int(bb)
        rg = int(rg)
        cnt = int(cnt)
        pay = (312*bb) + (104*rg) - (cnt/35)*50
        pay = int(pay)
        total += pay
        
        d = Data(store_name='コンサートホール荒川', name='マイジャグラーIII', number=num,bigbonus=bb, date=yesterday, regularbonus=rg, count=cnt,payout=pay)
        d.save()
    

# GOGOジャグラー 

    url = 'https://p-ken.jp/p-charakawa/bonus/lot?ps_div=2&cost=21.28&model_nm=GOGO%BC%DE%AC%B8%DE%D7%B0&day=' + str(scrape_day) + '&mode='
    response = request.urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')
    find = soup.findAll('table')
    find = soup.findAll(id='dataTable')
    find = soup.findAll('td')

    list = []
    for row in find:
        row = row.text
        list.append(row)

    
    
    new_list = []
    for i in list[9:58]:
        num = i.replace('\r\n', '')
        num = num.replace("  ", "")
        new_list.append(num)
    mylist = [item for item in new_list if item != '']
    length = len(mylist)
    n=0
    s=4
    mm_list = []
    for i in mylist:
        mm_list.append(mylist[n:n+s:1])
        n += s
        if n >= length:
            break
    
    
    for i in mm_list:
        num = i[0]
        bb = i[1]
        rg = i[2]
        cnt = i[3]
        num = int(num)
        bb = int(bb)
        rg = int(rg)
        cnt = int(cnt)
        pay = (312*bb) + (104*rg) - (cnt/34)*50
        pay = int(pay)
        total += pay
        
        d = Data(store_name='コンサートホール荒川', name='GOGOジャグラー', number=num,bigbonus=bb, date=yesterday, regularbonus=rg, count=cnt,payout=pay)
        d.save()
   

# ミラクルジャグラー 

    url = 'https://p-ken.jp/p-charakawa/bonus/lot?ps_div=2&cost=21.28&model_nm=%BD%B0%CA%DF%B0%D0%D7%B8%D9%BC%DE%AC%B8%DE%D7%B0&day=' + str(scrape_day) + '&mode='
    response = request.urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')
    find = soup.findAll('table')
    find = soup.findAll(id='dataTable')
    find = soup.findAll('td')

    list = []
    for row in find:
        row = row.text
        list.append(row)

    
    
    new_list = []
    
    for i in list[9:28]:
        num = i.replace('\r\n', '')
        num = num.replace("  ", "")
        new_list.append(num)
    mylist = [item for item in new_list if item != '']
    length = len(mylist)
    n=0
    s=4
    mm_list = []
    for i in mylist:
        mm_list.append(mylist[n:n+s:1])
        n += s
        if n >= length:
            break

    
    
    for i in mm_list:
        num = i[0]
        bb = i[1]
        rg = i[2]
        cnt = i[3]
        num = int(num)
        bb = int(bb)
        rg = int(rg)
        cnt = int(cnt)
        pay = (312*bb) + (104*rg) - (cnt/34)*50
        pay = int(pay)
        total += pay
        
        d = Data(store_name='コンサートホール荒川', name='ｽｰﾊﾟｰﾐﾗｸﾙｼﾞｬｸﾞﾗｰ', number=num,bigbonus=bb, date=yesterday, regularbonus=rg, count=cnt,payout=pay)
        d.save()

    t = TotalPay(total_pay=total, date=yesterday)
    t.save()

    
