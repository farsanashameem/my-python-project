from django.urls import path, include
from . import views
app_name='doctor'
urlpatterns = [
    path('doctorslog',views.logfun,name='login'),
    path('dochome',views.homefun,name='home')
]
