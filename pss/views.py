from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Data, TotalPay
from . forms import DataForm
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


class StoreNameView(ListView):
    model = Data
    template_name = 'scrape_ps/pss_list.html'

    def queryset(self):
        i = Data.objects.distinct().values_list('store_name')
        namelist =[]
        for n in i:
            stn = str(n).strip(")'(")
            stn = stn.rstrip("',")
            namelist.append(stn)
        return namelist
        
class DatalistView(ListView):
    model = Data
    template_name = 'scrape_ps/data_list.html'

    def queryset(self):
        return Data.objects.all()

class TotalPayView(ListView):
    model = TotalPay
    template_name = 'scrape_ps/total_pay.html'

    def queryset(self):
        return TotalPay.objects.all()


# class DateListView(ListView):
#     model = Data
#     template_name = 'scrape_ps/date_list.html'

#     def queryset(self):
#         i =Data.objects.distinct().values_list('date').order_by('-date')
#         datelist = []
#         for n in i:
#             dt = str(n).lstrip('(datetime.date(')
#             dt = dt.rstrip('),)')
#             dt = dt.replace(',', '/')
#             dt = dt.replace(' ', '')
#             datelist.append(dt)
        
#         context = {
#             'year' : 1,
#             'month' : 2,
#             'day' : 3,
#         }

#         return datelist

# class SelectDaysView(ListView):
#     model = Data

#     def queryset(self):
#         return Data.objects.filter(date=year + '-' + month + '-' + day)


