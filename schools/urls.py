from django.urls import path
from . import views

urlpatterns = [
    path('',views.sec_ON_schools, name = 'index'),
    path('elementaryschool_ON',views.ele_ON_schools, name = 'ele_ON'),
    path('elementaryschool_BC',views.ele_BC_schools, name = 'ele_BC'),
    path('secondaryschool_BC',views.sec_BC_schools, name = 'sec_BC'),
    path('search/', views.search, name='search'),
    path('get-cities/', views.get_cities, name='get_cities'),
]