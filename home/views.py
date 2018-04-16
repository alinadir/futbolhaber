from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect
from .models import SosyalMedia,Yorum,Yazi,Puan
from ligler.models import Fikstur,Oyuncu
from django.utils.text import slugify
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib import messages
#from django.views.decorators.csrf import csrf_exempt

def home_view(request):
	
	fikstur= Fikstur.objects.filter(mac_saati__range=["2018-04-16", "2018-04-24"])
	takımlar=Puan.objects.all()
	yazılar=Yazi.objects.all()[0:15]
	yazıbjk = Yazi.objects.filter(konu__isim="Beşiktaş")[0:10]
	yazıgs = Yazi.objects.filter(konu__isim="Galatasaray")[0:10]
	yazıfb = Yazi.objects.filter(konu__isim="Fenerbahçe")[0:10]
	yazıts = Yazi.objects.filter(konu__isim="Trabzonspor")[0:10]
	yazıavr = Yazi.objects.filter(konu__isim="Avrupa")[0:10]
	
	
	bjkfikstur=Fikstur.objects.filter(Q(takım1__isim="Beşiktaş")| Q(takım2__isim="Beşiktaş")).filter(mac_saati__range=["2018-04-01", "2018-08-10"])
	gsfikstur=Fikstur.objects.filter(Q(takım1__isim="Galatasaray")| Q(takım2__isim="Galatasaray")).filter(mac_saati__range=["2018-04-01", "2018-08-10"])
	fbfikstur=Fikstur.objects.filter(Q(takım1__isim="Fenerbahçe")| Q(takım2__isim="Fenerbahçe")).filter(mac_saati__range=["2018-04-01", "2018-08-10"])
	tsfikstur=Fikstur.objects.filter(Q(takım1__isim="Trabzonspor")| Q(takım2__isim="Trabzonspor")).filter(mac_saati__range=["2018-04-01", "2018-08-10"])
	
	sosyaller = SosyalMedia.objects.all()[0:35]
	#sosyaller1 = SosyalMedia.objects.all()[40:54]
	bjk = SosyalMedia.objects.filter(konu__isim__icontains="Beşiktaş")[0:35]
	fb = SosyalMedia.objects.filter(konu__isim__icontains="Fenerbahçe")[0:35]
	gs = SosyalMedia.objects.filter(konu__isim__icontains="Galatasaray")[0:35]
	ts = SosyalMedia.objects.filter(konu__isim__icontains="Trabzonspor")[0:35]
	avr = SosyalMedia.objects.filter(konu__isim__icontains="Avrupa")[0:35]
	
	gol = Oyuncu.objects.order_by('-gol_sayısı','-asist_sayısı')[0:10]
	asist = Oyuncu.objects.order_by('-asist_sayısı','-gol_sayısı')[0:10]
	kartlar = Oyuncu.objects.order_by('-kırmızı_sayısı','-sarıkart_sayısı')[0:10]
	
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
		#'sosyaller1':sosyaller1,
		'bjk':bjk,
		'fb':fb,
		'gs':gs,
		'ts':ts,
		'avr':avr,
		'takımlar':takımlar,
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
		
		
	}	
	#if request.GET:
	#	a=request.GET['key1']
	#	Konu.objects.create(isim=a)
		#print(context)
		
		
		
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
		aaa = sosyaller.filter(
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
	

	