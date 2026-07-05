
from django.contrib import admin
from django.urls import path,include
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/',include('accounts.urls')),
    path('',index, name="home"),
    path('create/',create, name="create"),
    path('update/<id>/',update, name="update"),
    path('delete/<id>/',delete, name="delete"),
]