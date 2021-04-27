from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from ... models import Data, TotalPay

from django.urls import reverse_lazy
import csv
import urllib
from urllib import request
from bs4 import BeautifulSoup
import ssl
import datetime
import pandas as pd
import io,sys
import calendar
from django.db.models import Sum


def show_line_graph(request):
    line_data = TotalPay.objects.all()
    line_list =['1']

    date_list = []
    for i in line_data:
        date_list.append((i.date.strftime('%Y/%m/%d')[:9]))
    x_label = date_list.sort(reverse=False)
    print(date_list)
    monthly_sum_data = []
    for i in range(len(x_label)):
       year,month,day = x_label[i].split("/")
       month_range = calendar.monthrange(int(year),int(month))[1]
       first_date = year + '-' + month +'-' + '01'
       last_date = year + '-' + month + '-' + str(month_range)
       total_of_month = TotalPay.objects.filter(date__range=(first_date, last_date))
       category_total = total_of_month.values('date').annotate(total_price=Sum('total_pay'))
       for j in range(len(category_total)):
           money = category_total[j]['total_price']
           category = Category.objects.get(pk=category_total[j]['category'])
           monthly_sum_data.append([x_label[i], category.category_name,money])
    #折れ線グラフのボーダーカラー色の設定      
    border_color_list=['254,97,132,0.8','54,164,235,0.8','0,255,65,0.8','255,241,15,0.8',\
                      '255,94,25,0.8','84,77,203,0.8','204,153,50,0.8','214,216,165,0.8',\
                      '33,30,45,0.8','52,38,89,0.8']
    border_color =[]
    for x,y in zip(line_list, border_color_list):
        border_color.append([x,y])
       
    background_color_list=['254,97,132,0.5','54,164,235,0.5','0,255,65,0.5','255,241,15,0.5',\
                          '255,94,25,0.5','84,77,203,0.5','204,153,50,0.5','214,216,165,0.5'\
                          '33,30,45,0.5','52,38,89,0.5']
    background_color =[]
    for x,y in zip(line_list, background_color_list):
        background_color.append([x,y])
    matrix_list =[]
    for item_label in x_label:
        for item_category in category_list:
            matrix_list.append([item_label, item_category, 0])
   
    """matrix_listとmonthlysum_dataに対して、「年月+カテゴリ」の
    組み合わせが一致する要素に対してmatrix_listの金額（０円）を
    monthly_sum_dataの金額で上書きする。
    """
    for yyyy_mm,category,total in monthly_sum_data:
        for i,data in enumerate(matrix_list):
            if data[0]==yyyy_mm and data[1] ==category:
                matrix_list[i][2] = total

    return render(request, 'scrape_ps/line.html',{
       'x_label': x_label,
       'category_list': line_list,
       'border_color': border_color,
       'background_color': background_color,
       'matrix_list': matrix_list,
                } )

