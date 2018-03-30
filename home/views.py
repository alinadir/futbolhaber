from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect
from .models import SosyalMedia,Yorum,TV,Yazi
from ligler.models import Klup,Fikstur,Gol,Asist,Kart
from django.utils.text import slugify
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.


# Create your views here.
def home_view(request):#ana sayfamızın
	fikstur= Fikstur.objects.filter(hafta="2")
	takımlar=Klup.objects.all()
	yazılar=Yazi.objects.all()
	yazıbjk = yazılar.filter(konu__isim="Beşiktaş")
	yazıgs = yazılar.filter(konu__isim="Galatasaray")
	yazıfb = yazılar.filter(konu__isim="Fenerbahçe")
	yazıts = yazılar.filter(konu__isim="Trabzonspor")
	tv=TV.objects.all()
	
	bjkfikstur=Fikstur.objects.filter(Q(takım1__isim="Beşiktaş")| Q(takım2__isim="Beşiktaş"))[0:2]
	gsfikstur=Fikstur.objects.filter(Q(takım1__isim="Galatasaray")| Q(takım2__isim="Galatasaray"))[0:2]
	fbfikstur=Fikstur.objects.filter(Q(takım1__isim="Fenerbahçe")| Q(takım2__isim="Fenerbahçe"))[0:2]
	tsfikstur=Fikstur.objects.filter(Q(takım1__isim="Trabzonspor")| Q(takım2__isim="Trabzonspor"))[0:2]
	
	sosyaller = SosyalMedia.objects.all()
	bjk = SosyalMedia.objects.filter(konu__isim__icontains="Beşiktaş")
	fb = SosyalMedia.objects.filter(konu__isim__icontains="Fenerbahçe")
	gs = SosyalMedia.objects.filter(konu__isim__icontains="Galatasaray")
	ts = SosyalMedia.objects.filter(konu__isim__icontains="Trabzonspor")
	
	gol = Gol.objects.all()
	asist = Asist.objects.all()
	kartlar = Kart.objects.all()
	
	golbjk = Gol.objects.filter(takım__isim="Beşiktaş")
	asistbjk = Asist.objects.filter(takım__isim="Beşiktaş")
	kartlarbjk = Kart.objects.filter(takım__isim="Beşiktaş")

	golfb = Gol.objects.filter(takım__isim="Fenerbahçe")
	asistfb = Asist.objects.filter(takım__isim="Fenerbahçe")
	kartlarfb = Kart.objects.filter(takım__isim="Fenerbahçe")
	
	golts = Gol.objects.filter(takım__isim="Trabzonspor")
	asistts = Asist.objects.filter(takım__isim="Trabzonspor")
	kartlarts = Kart.objects.filter(takım__isim="Trabzonspor")
	
	golgs = Gol.objects.filter(takım__isim="Galatasaray")
	asistgs = Asist.objects.filter(takım__isim="Galatasaray")
	kartlargs = Kart.objects.filter(takım__isim="Galatasaray")
	
	
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
		'takımlar':takımlar,
		'tv':tv,
		'yazılar':yazılar,
		'yazıbjk':yazıbjk,
		'yazıgs':yazıgs,
		'yazıfb':yazıfb,
		'yazıts':yazıts,
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
	return render(request,"home/home.html",context)#home.html in dire
	

	
def sosyal_detail(request,slug):#ana sayfamızın
	sosyal=get_object_or_404(SosyalMedia, slug =slug)
	form = CommentForm(request.POST or None)
	if form.is_valid():
		comment=form.save(commit=False)
		#comment.user = request.user
		comment.post = sosyal
		comment.save()
		
		print(comment)
		return redirect("homee:home")
	
	sosyaller=SosyalMedia.objects.filter(isim=sosyal.isim).exclude(slug=slug)
	
	context = {
		'sosyal':sosyal,
		'sosyaller':sosyaller,
		'form':form,
	}
	
	return render(request,"home/sdetail.html",context)#home.html in dire
	

	