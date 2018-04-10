from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect
from .models import SosyalMedia,Yorum,TV,Yazi,Puan
from ligler.models import Fikstur,Oyuncu
from django.utils.text import slugify
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib import messages




# Create your views here.


# Create your views here.
def home_view(request):#ana sayfamızın
	a=0
	if request.GET:
		a=request.GET['key1']
		print(a)
		
		
	
	fikstur= Fikstur.objects.filter(mac_saati__range=["2018-04-07", "2018-04-10"])
	takımlar=Puan.objects.all()
	yazılar=Yazi.objects.all()
	yazıbjk = yazılar.filter(konu__isim="Beşiktaş")
	yazıgs = yazılar.filter(konu__isim="Galatasaray")
	yazıfb = yazılar.filter(konu__isim="Fenerbahçe")
	yazıts = yazılar.filter(konu__isim="Trabzonspor")
	yazıavr = yazılar.filter(konu__isim="Avrupa")
	tv=TV.objects.all()
	
	bjkfikstur=Fikstur.objects.filter(Q(takım1__isim="Beşiktaş")| Q(takım2__isim="Beşiktaş")).filter(mac_saati__range=["2018-04-01", "2018-08-10"])
	gsfikstur=Fikstur.objects.filter(Q(takım1__isim="Galatasaray")| Q(takım2__isim="Galatasaray")).filter(mac_saati__range=["2018-04-01", "2018-08-10"])
	fbfikstur=Fikstur.objects.filter(Q(takım1__isim="Fenerbahçe")| Q(takım2__isim="Fenerbahçe")).filter(mac_saati__range=["2018-04-01", "2018-08-10"])
	tsfikstur=Fikstur.objects.filter(Q(takım1__isim="Trabzonspor")| Q(takım2__isim="Trabzonspor")).filter(mac_saati__range=["2018-04-01", "2018-08-10"])
	
	sosyaller = SosyalMedia.objects.all()
	bjk = SosyalMedia.objects.filter(konu__isim__icontains="Beşiktaş")
	fb = SosyalMedia.objects.filter(konu__isim__icontains="Fenerbahçe")
	gs = SosyalMedia.objects.filter(konu__isim__icontains="Galatasaray")
	ts = SosyalMedia.objects.filter(konu__isim__icontains="Trabzonspor")
	avr = SosyalMedia.objects.filter(konu__isim__icontains="Avrupa") 
	
	gol = Oyuncu.objects.order_by('-gol_sayısı','-asist_sayısı')
	asist = Oyuncu.objects.order_by('-asist_sayısı','-gol_sayısı',)
	kartlar = Oyuncu.objects.order_by('-kırmızı_sayısı','-sarıkart_sayısı')
	
	golbjk = Oyuncu.objects.filter(takım__isim="Beşiktaş").order_by('-gol_sayısı','asist_sayısı')
	asistbjk = Oyuncu.objects.filter(takım__isim="Beşiktaş").order_by('-asist_sayısı','gol_sayısı')
	kartlarbjk = Oyuncu.objects.filter(takım__isim="Beşiktaş").order_by('-kırmızı_sayısı','-sarıkart_sayısı')

	golfb = Oyuncu.objects.filter(takım__isim="Fenerbahçe").order_by('-gol_sayısı','asist_sayısı')
	asistfb = Oyuncu.objects.filter(takım__isim="Fenerbahçe").order_by('-asist_sayısı','gol_sayısı')
	kartlarfb = Oyuncu.objects.filter(takım__isim="Fenerbahçe").order_by('-kırmızı_sayısı','-sarıkart_sayısı')
	
	golts = Oyuncu.objects.filter(takım__isim="Trabzonspor").order_by('-gol_sayısı','asist_sayısı')
	asistts = Oyuncu.objects.filter(takım__isim="Trabzonspor").order_by('-asist_sayısı','gol_sayısı')
	kartlarts = Oyuncu.objects.filter(takım__isim="Trabzonspor").order_by('-kırmızı_sayısı','-sarıkart_sayısı')
	
	golgs = Oyuncu.objects.filter(takım__isim="Galatasaray").order_by('-gol_sayısı','asist_sayısı')
	asistgs = Oyuncu.objects.filter(takım__isim="Galatasaray").order_by('-asist_sayısı','gol_sayısı')
	kartlargs = Oyuncu.objects.filter(takım__isim="Galatasaray").order_by('-kırmızı_sayısı','-sarıkart_sayısı')
	
	
	query = request.GET.get("q")
	if query:
		print(query)
		aaa = SosyalMedia.objects.filter(
		Q(isim__isim__icontains=query)|
		Q(content1__icontains=query)|
		Q(content2__icontains=query)|
		Q(konu__isim__icontains=query)
		).distinct()
		if aaa:
			sosyaller = aaa
			
	context = {
		'sosyaller':sosyaller,
		'bjk':bjk,
		'fb':fb,
		'gs':gs,
		'ts':ts,
		'avr':avr,
		'takımlar':takımlar,
		'tv':tv,
		'yazılar':yazılar,
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
		'a',a,
	}	
	return render(request,"home/home.html",context)#home.html in dire
	

	
def sosyal_detail(request,slug):#ana sayfamızın
	sosyal=get_object_or_404(SosyalMedia, slug =slug)
	form = CommentForm(request.POST or None)
	if form.is_valid():
		comment=form.save(commit=False)
		#comment.user = request.user
		comment.post = sosyal
		comment.save()
		messages.success(request,'Yorumunuz başarlı bir şekilde oluşturuldu.',extra_tags='yorum-eklendi')
		print(comment)
		return redirect("homee:home")
	
	sosyaller=SosyalMedia.objects.filter(isim=sosyal.isim).exclude(slug=slug)
	query = request.GET.get("q")
	if query:
		print(query)
		aaa = SosyalMedia.objects.filter(
		Q(isim__isim__icontains=query)|
		Q(content1__icontains=query)|
		Q(content2__icontains=query)|
		Q(konu__isim__icontains=query)
		).distinct()
		if aaa:
			sosyaller = aaa
	
	
	paginator = Paginator(sosyaller, 5) # Show 25 contacts per page
	
	page = request.GET.get('page')
	
	try:
		sosyaller = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		sosyaller = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		sosyaller = paginator.page(paginator.num_pages)
	
	context = {
		'sosyal':sosyal,
		'sosyaller':sosyaller,
		'form':form,
	}
	
	return render(request,"home/sdetail.html",context)#home.html in dire
	

	