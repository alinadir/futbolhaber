#from django.contrib import admin
#from django.urls import path
from django.conf.urls import url,include
from home.views import home_view,sosyal_detail


app_name='homee'
urlpatterns = [
    
	url(r'^$', home_view, name="home"),
	#url(r'^(?P<slug>[\w-]+)/$', home_detail, name="detail"),
	url(r'^(?P<slug>[\w-]+)/$', sosyal_detail, name="sdetail"),
#url içerisinde verilen name.lere url metoduyla html dosyaları içerisinden ulaşabiliriz.
]


##3