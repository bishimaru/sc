from django.db import models
from datetime import datetime 




class Data(models.Model):
    class Meta:
        db_table = 'data'
        verbose_name='データ一覧'
        verbose_name_plural ='データ一覧'
    store_name = models.CharField(max_length=100, default='コンサートホール', verbose_name='店舗名')
    name = models.CharField(max_length=100, verbose_name='機種名')
    number = models.IntegerField(verbose_name='台番号')
    date = models.DateField(verbose_name='日付', default=datetime.now())
    bigbonus = models.IntegerField(verbose_name='BB')
    regularbonus = models.IntegerField(verbose_name='RB')
    count =models.IntegerField(verbose_name='総回転数')
    payout = models.IntegerField(verbose_name='差枚数')
    memo = models.CharField(max_length=50, verbose_name='メモ', blank=True, null=True)

    def __str__(self):
       return self.name
       
class TotalPay(models.Model):
    class Meta:
        db_table = 'pay'
        verbose_name='差枚数'
        verbose_name_plural ='差枚数'

    total_pay = models.IntegerField(verbose_name='総差枚数')
    date = models.DateField(verbose_name='日付', default=datetime.now())


