from django.conf.urls import url
from ligler.views import ligler_view

app_name='ligler'
urlpatterns = [
    
	
	#url(r'^ligler/superlig/$', ligler_view, name="super_lig"),
	url(r'^ligler/(?P<a>[\w-]+)/$', ligler_view, name="super_lig"),
	
	
#url içerisinde verilen name.lere url metoduyla html dosyaları içerisinden ulaşabiliriz.
]