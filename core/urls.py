from . import views
from django.urls import path

app_name ='CORE'

urlpatterns = [
    path('',views,name=""),
] 