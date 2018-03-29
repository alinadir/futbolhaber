from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect
from .models import SosyalMedia,Comment,Club,Hafta,Fikstur,TV,Yazi
from django.utils.text import slugify
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.


# Create your views here.
def home_view(request):#ana sayfamızın
	takımlar=Club.objects.all()
	yazılar=Yazi.objects.all()
	yazıbjk = yazılar.filter(ilgi="Beşiktaş")
	yazıgs = yazılar.filter(ilgi="Galatasaray")
	yazıfb = yazılar.filter(ilgi="Fenerbahçe")
	yazıts = yazılar.filter(ilgi="Trabzonspor")
	tv=TV.objects.all()
	fikstur=Fikstur.objects.all()
	#birinci_fikstur = Fikstur.objects.filter(hafta="birinci")
	bjkfikstur=fikstur.filter(Q(takım1__isim="Beşiktaş")| Q(takım2__isim="Beşiktaş"))
	gsfikstur=fikstur.filter(Q(takım1__isim="Galatasaray")| Q(takım2__isim="Galatasaray"))
	fbfikstur=fikstur.filter(Q(takım1__isim="Fenerbahçe")| Q(takım2__isim="Fenerbahçe"))
	tsfikstur=fikstur.filter(Q(takım1__isim="Trabzonspor")| Q(takım2__isim="Trabzonspor"))
	print(bjkfikstur)
	print(tsfikstur)
	print(gsfikstur)
	print(fbfikstur)
	sosyaller = SosyalMedia.objects.all()
	bjk = SosyalMedia.objects.filter(konu__icontains="Beşiktaş")
	fb = SosyalMedia.objects.filter(konu__icontains="Fenerbahçe")
	gs = SosyalMedia.objects.filter(konu__icontains="Galatasaray")
	ts = SosyalMedia.objects.filter(konu__icontains="Trabzonspor")
	
	query = request.GET.get("q")
	if query:
		print(query)
		aaa = SosyalMedia.objects.filter(
		Q(isim__isim__icontains=query)|
		Q(content1__icontains=query)|
		Q(content2__icontains=query)|
		Q(konu__icontains=query)
		).distinct()
		if aaa:
			sosyaller = aaa
			
		
	
	
	paginator = Paginator(sosyaller, 20) # Show 25 contacts per page
	
	page = request.GET.get('page')
	
	try:
		sosyaller = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		sosyaller = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		sosyaller = paginator.page(paginator.num_pages)
	
	
	
		
	a={"bir":"1",
	"2":"2",
	"3":"3",
	"4":"4"}
	
	#ilk_haber=haberler[0:1]
	#print(ilk_haber)
	#oniki_haber=haberler[1:12]
	#print(oniki_haber)
	#ilk rowun kenardaki 2 thumbnaili
	#ikinci_row = haberler[12:21]
	#Sıralama=Puan.objects.all()[:4]
	#Sıralama=Puan.objects.all()
	Commentss=Comment.objects.all()
	
	
	
	
	
	context = {
		#'haber1':ilk_haber,
		#'haberler':oniki_haber,
		#'ikinci_row': ikinci_row,
		#'sosyaller2':sosyaller2,
		'sosyaller':sosyaller,
		'bjk':bjk,
		'fb':fb,
		'gs':gs,
		'ts':ts,
		#'fikstur':Fiks.objects.all()[:1],
		#'Puan_Durumu1':Sıralama,
		#'pre_fikstur':PremierFiks.objects.all()[:1],
		#'pre_Puan_Durumu1':PremierPuan.objects.all()[:4],
		'a':a,
		'page':page,
		'takımlar':takımlar,
		'fikstur':fikstur,
		'tv':tv,
		'yazılar':yazılar,
		'yazıbjk':yazıbjk,
		'yazıgs':yazıgs,
		'yazıfb':yazıfb,
		'yazıts':yazıts,
		'bjkfikstur':bjkfikstur,
		'tsfikstur':tsfikstur,
		'gsfikstur':gsfikstur,	
		'fbfikstur':fbfikstur,
		
		'comment':Commentss,
		
		
		
	}	
	return render(request,"home1.html",context)#home.html in dire
	

	
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
	
	return render(request,"sdetail.html",context)#home.html in dire
	

	