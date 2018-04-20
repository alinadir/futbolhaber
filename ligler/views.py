from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect
from home.models import SosyalMedia,Yorum,Yazi,Puan
from .models import Fikstur,Oyuncu
from django.utils.text import slugify
from home.forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib import messages





# Create your views here.
def ligler_view(request):#ana sayfamızın
	#oyuncular1 = Oyuncu.objects.order_by("toplam_gol_sayısı")
	fikstur= Fikstur.objects.filter(mac_saati__range=["2018-02-18", "2018-04-24"])
	#yazılar=Yazi.objects.all()[0:15]
	yazıbjk = Yazi.objects.filter(konu__isim="Beşiktaş")[0:10]
	yazıgs = Yazi.objects.filter(konu__isim="Galatasaray")[0:10]
	yazıfb = Yazi.objects.filter(konu__isim="Fenerbahçe")[0:10]
	yazıts = Yazi.objects.filter(konu__isim="Trabzonspor")[0:10]
	yazıavr = Yazi.objects.filter(konu__isim="Avrupa")[0:10]
	
	
	bjkfikstur=Fikstur.objects.filter(Q(takım1__isim="Beşiktaş")| Q(takım2__isim="Beşiktaş")).filter(mac_saati__range=["2018-04-01", "2018-08-10"])
	gsfikstur=Fikstur.objects.filter(Q(takım1__isim="Galatasaray")| Q(takım2__isim="Galatasaray")).filter(mac_saati__range=["2018-04-01", "2018-08-10"])
	fbfikstur=Fikstur.objects.filter(Q(takım1__isim="Fenerbahçe")| Q(takım2__isim="Fenerbahçe")).filter(mac_saati__range=["2018-04-01", "2018-08-10"])
	tsfikstur=Fikstur.objects.filter(Q(takım1__isim="Trabzonspor")| Q(takım2__isim="Trabzonspor")).filter(mac_saati__range=["2018-04-01", "2018-08-10"])
	

	
	gol = Oyuncu.objects.order_by('-gol_sayısı','-asist_sayısı')[0:10]
	asist = Oyuncu.objects.order_by('-asist_sayısı','-gol_sayısı')[0:10]
	kartlar = Oyuncu.objects.order_by('-kırmızı_sayısı','-sarıkart_sayısı')[0:10]
	
	golbjk = Oyuncu.objects.filter(takım__isim="Beşiktaş").order_by('-gol_sayısı','asist_sayısı')
	asistbjk = Oyuncu.objects.filter(takım__isim="Beşiktaş").order_by('-asist_sayısı','-gol_sayısı')
	kartlarbjk = Oyuncu.objects.filter(takım__isim="Beşiktaş").order_by('-kırmızı_sayısı','-sarıkart_sayısı')
	
	golfb = Oyuncu.objects.filter(takım__isim="Fenerbahçe").order_by('-gol_sayısı','asist_sayısı')
	asistfb = Oyuncu.objects.filter(takım__isim="Fenerbahçe").order_by('-asist_sayısı','-gol_sayısı')
	kartlarfb = Oyuncu.objects.filter(takım__isim="Fenerbahçe").order_by('-kırmızı_sayısı','-sarıkart_sayısı')
	
	golts = Oyuncu.objects.filter(takım__isim="Trabzonspor").order_by('-gol_sayısı','asist_sayısı')
	asistts = Oyuncu.objects.filter(takım__isim="Trabzonspor").order_by('-asist_sayısı','-gol_sayısı')
	kartlarts = Oyuncu.objects.filter(takım__isim="Trabzonspor").order_by('-kırmızı_sayısı','-sarıkart_sayısı')
	
	golgs = Oyuncu.objects.filter(takım__isim="Galatasaray").order_by('-gol_sayısı','asist_sayısı')
	asistgs = Oyuncu.objects.filter(takım__isim="Galatasaray").order_by('-asist_sayısı','-gol_sayısı')
	kartlargs = Oyuncu.objects.filter(takım__isim="Galatasaray").order_by('-kırmızı_sayısı','-sarıkart_sayısı')
	
	context = {
		'yazıbjk':yazıbjk,
		'yazıgs':yazıgs,
		'yazıfb':yazıfb,
		'yazıts':yazıts,
		'yazıavr':yazıavr,
		'fikstur':fikstur,
		'bjkfikstur':bjkfikstur,
		'fbfikstur':fbfikstur,
		'gsfikstur':gsfikstur,
		'tsfikstur':tsfikstur,
		'gol':gol,
		'asist':asist,
		'kartlar':kartlar,
		'golbjk':golbjk,
		'asistbjk':asistbjk,
		'kartlarbjk':kartlarbjk,
		'golfb':golfb,
		'asistfb':asistfb,
		'kartlarfb':kartlarfb,	
		'golgs':golgs,
		'asistgs':asistgs,
		'kartlargs':kartlargs,
		'golts':golts,
		'asistts':asistts,
		'kartlarts':kartlarts,
		
		
	}	
		
	return render(request,"ligler/superlig/home.html",context)#home.html in dire
	

