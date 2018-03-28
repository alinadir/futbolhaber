from django.shortcuts import render
from home.models import Haberler
from ligler.models import  Fiks,Puan,Hafta,Takım

# Create your views here.

def besiktas(request):#ana sayfamızın
	haberler = Haberler.objects.filter(haberin_konusu="Beşiktaş")[:5]
	
	context= {
	'haberler':haberler,
	'haberler':haberler,
	
	}
	return render(request,"club/besiktas/besiktas.html",context)
	
def fenerbahce(request):#ana sayfamızın
	haberler = Haberler.objects.filter(haberin_konusu="Fenerbahçe")[:5]
	return render(request,"club/fenerbahce/fenerbahce.html",{'haberler':haberler})
	
def galatasaray(request):#ana sayfamızın
	haberler = Haberler.objects.filter(haberin_konusu="Galatasaray")[:5]
	return render(request,"club/galatasaray/galatasaray.html",{'haberler':haberler})

def trabzonspor(request):#ana sayfamızın
	haberler = Haberler.objects.filter(haberin_konusu="Trabzonspor")[:5]
	return render(request,"club/trabzonspor/trabzonspor.html",{'haberler':haberler})