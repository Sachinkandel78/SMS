from django.contrib import admin
from django.urls import path
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('create/',create),
    path('update/<id>/',update),
    path('delete/<id>/',delete),

]