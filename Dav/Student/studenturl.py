from django.urls import path,include
from . import views
urlpatterns =[
    path('',views.home,name="home"),
    path("addtwo",views.sum_page,name="Sum App"),
    path("find_sum",views.sum_logic,name="Add two number"),
    path("multi",views.multiplication,name="Multiplication Example"),
    
]



