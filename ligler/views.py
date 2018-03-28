from django.shortcuts import render
from ligler.models import Fiks,Puan,Hafta,Takım
from home.models import Haberler

# Create your views here.
def ligler_view(request):#ana sayfamızın
	haberler = Haberler.objects.filter(haberin_konusu="Beşiktaş")[:5]
	#Puan_Durumu = PuanDurumu.objects.all()
	Puan_Durumu1 = PuanDurumu.objects.all()[0:6]
	#sosyaller = SosyalMedia.objects.all()[0:10]
	ilk_haber=haberler[0:1]
	oniki_haber=haberler[1:12]
	#print(oniki_haber)
	#ilk rowun kenardaki 2 thumbnaili
	ikinci_row = haberler[12:21]
	
	a=Hafta.objects.get(hafta="1.Hafta")
	b=a.fiks_set.all()
	c=a.puan_set.all()
		
	context = {
		'haber1':ilk_haber,
		'haberler':oniki_haber,
		'ikinci_row': ikinci_row,
		#'Puan_Durumu':Puan_Durumu,
		'1.Fik':b,
		'2.Puan':c,
		'Puan_Durumu1':Puan_Durumu1,
	}
		
	return render(request,"ligler/superlig/home.html",context)#home.html in dire