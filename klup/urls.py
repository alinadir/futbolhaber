from django.conf.urls import url,include
from klup.views import besiktas,fenerbahce,galatasaray,trabzonspor

app_name='klup'
urlpatterns = [
    
	
	url(r'^klup/besiktas/$', besiktas, name="BJK"),
	url(r'^klup/fenerbahce/$', fenerbahce, name="FB"),
	url(r'^klup/galatasaray/$', galatasaray, name="GS"),
	url(r'^klup/trabzonspor/$', trabzonspor, name="TS"),
#url içerisinde verilen name.lere url metoduyla html dosyaları içerisinden ulaşabiliriz.
]