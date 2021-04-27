from django.urls import path

from . import views

app_name = 'scrape_ps'

urlpatterns = [
    path('pss_list/', views.StoreNameView.as_view(), name='pss_list'),
    path('data_list/', views.DatalistView.as_view(), name='data_list'),
    # path('date_list/', views.DateListView.as_view(), name='date_list'),
    # path('ss/', views.SelectDaysView.as_view(), name='ss'),
    path('total_pay/', views.TotalPayView.as_view(), name='total_pay'),
    # path('line/',views.show_line_graph, name='line'),
    
]