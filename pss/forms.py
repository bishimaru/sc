from django import forms
from .models import Data
import csv
import urllib
from urllib import request
from bs4 import BeautifulSoup
import ssl
import datetime
import pandas as pd
import io,sys

class DataForm(forms.ModelForm):
   """
   新規データ登録画面用のフォーム定義
   """
   
   class Meta:
       model = Data
       fields =['name', 'number', 'date', 'bigbonus', 'regularbonus', 'count', 'payout', 'memo']
         