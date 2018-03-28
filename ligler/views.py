from django.shortcuts import render
from .models import Ülke,Oyuncu,Takım,Fikstur,Hafta,Sezon,Yardımcılar,Hoca,Yoneticiler,Stadyum,İdman,LigKupa
from home.models import Haberler
from django.db.models import Q
from operator import add



# Create your views here.
def ligler_view(request):#ana sayfamızın
	oyuncular1 = Oyuncu.objects.order_by("toplam_gol_sayısı")
	oyuncular2 = Oyuncu.objects.order_by("toplam_asist_sayısı")
	print(oyuncular1)
	print(oyuncular2)
	takımlar =Takım.objects.all()
	fikstur1 = Fikstur.objects.filter(hafta="1",mac_saati__range=["2018-03-01", "2018-03-26"])
	fikstur2= Fikstur.objects.filter(hafta="2",mac_saati__range=["2018-03-01", "2018-03-26"])
	haftalar=['1',"2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34"]
	durumlar =[]
	
	#Sample.objects.filter(date__range=["2011-01-01", "2011-01-31"])
	#Sample.objects.filter(date__year='2011', date__month='01')
	#queryset.filter(created_at__gte=datetime.date.today())
	#__gte (greater than or equal) and __lte (less than or equal)
	
	
	haftalar =["1","2"]
	fiksturler=[]
	fiksturler_ev_dep=[]
	for a in haftalar:
		fiksturler.append(hafta_hafta_takimlar(a))
		
	for a in haftalar:
		fiksturler_ev_dep.append(hafta_hafta_ev_dep(a))
	
	
		
	sıra = []
	sıra1 =[]
	genel_sıra = []
	for takım in takımlar:
			
			
		#sıra1 = sıra1.append([{'name':takım.isim,"durum":durum1}])
		sıra1.append([{'name':takım.isim,"durum":fiksturler[0][takım.isim]}])
			
		durum = takim_hafta_puan(fiksturler[0][takım.isim],fiksturler[1][takım.isim])
		sıra.append([{'name':takım.isim,"durum":durum}])
			
			
	#print(sıra)
	sıralama=sirala(sıra)
	sıralama1=sirala(sıra1)
	genel_sıra.append(sıralama)
	genel_sıra.append(sıralama1)
	
	context = {
		
		'sıra':sıra,
		'sıra1': sıra1,
		'sıralama':sıralama,
		'genel_sıra':genel_sıra,
		'fikstur1':fikstur1,
		'fikstur2':fikstur2,
	}
		
	return render(request,"ligler/superlig/home.html",context)#home.html in dire
	

def hafta_hafta_takimlar(a):
	hafta = Fikstur.objects.filter(hafta__kacıncı_hafta=a)
	neticeler = {}
	#print(hafta)
	for mac in hafta:
		#durum[mac.takım1.isim]=[mac.oynadıgı_mac1, mac.puan1, mac.averaj1, mac.galibiyet1, mac.maglubiyet1, mac.beraberlik1]
		#durum[mac.takım2.isim]=[mac.oynadıgı_mac2, mac.puan2, mac.averaj2, mac.galibiyet2, mac.maglubiyet2, mac.beraberlik2]
		#print(mac)
		neticeler[mac.takım1.isim] = [mac.oynadıgı_mac1, mac.galibiyet1, mac.beraberlik1, mac.maglubiyet1, mac.takım1_skor, mac.takım2_skor, mac.averaj1, mac.puan1,
									  mac.oynadıgı_mac1, mac.galibiyet1, mac.beraberlik1, mac.maglubiyet1, mac.takım1_skor, mac.takım2_skor, mac.averaj1, mac.puan1,
									  0,0, 0, 0, 0, 0, 0,0
									 ]
		#print(neticeler)
		neticeler[mac.takım2.isim] = [mac.oynadıgı_mac2,mac.galibiyet2,mac.beraberlik2, mac.maglubiyet2, mac.takım2_skor, mac.takım1_skor, mac.averaj2, mac.puan2,
									  0,0, 0, 0, 0, 0, 0,0,
									  mac.oynadıgı_mac2,mac.galibiyet2,mac.beraberlik2, mac.maglubiyet2, mac.takım2_skor, mac.takım1_skor, mac.averaj2, mac.puan2
									  ]
		#print(neticeler)
			
		
		
		
		
		#baba.append(bir)
		#baba.append(iki)
		#print(a)
		# newlist = sorted(a, key=lambda k: (k['durum'][0],k['durum'][1]))
		#a = [{'name':"Beşiktaş","durum":[1,1,3]},{'name':"Galatasaray","durum":[1,0,3]},{'name':"Fener","durum":[1,2,3]}]
	#print(neticeler)
	return neticeler
	
def hafta_hafta_ev_dep(a):
	hafta = Fikstur.objects.filter(hafta__kacıncı_hafta=a)
	ev_sahibi_neticeler= {}
	deplesman_neticeler= {}
	tum_neticeler = []
	#print(hafta)
	for mac in hafta:
		#durum[mac.takım1.isim]=[mac.oynadıgı_mac1, mac.puan1, mac.averaj1, mac.galibiyet1, mac.maglubiyet1, mac.beraberlik1]
		#durum[mac.takım2.isim]=[mac.oynadıgı_mac2, mac.puan2, mac.averaj2, mac.galibiyet2, mac.maglubiyet2, mac.beraberlik2]
		#print(mac)
		ev_sahibi_neticeler[mac.takım1.isim] = [mac.oynadıgı_mac1, mac.galibiyet1, mac.beraberlik1, mac.maglubiyet1, mac.takım1_skor, mac.takım2_skor, mac.averaj1, mac.puan1,
												mac.oynadıgı_mac1, mac.galibiyet1, mac.beraberlik1, mac.maglubiyet1, mac.takım1_skor, mac.takım2_skor, mac.averaj1, mac.puan1,
												0,0, 0, 0, 0, 0, 0,0
												]
		#print(neticeler)
		deplesman_neticeler[mac.takım2.isim] = [mac.oynadıgı_mac2,mac.galibiyet2,mac.beraberlik2, mac.maglubiyet2, mac.takım2_skor, mac.takım1_skor, mac.averaj2, mac.puan2,
												0,0, 0, 0, 0, 0, 0,0,
												mac.oynadıgı_mac2,mac.galibiyet2,mac.beraberlik2, mac.maglubiyet2, mac.takım2_skor, mac.takım1_skor, mac.averaj2, mac.puan2
												]
		#print(deplesman_neticeler)
			
		
		
		
		
		#baba.append(bir)
		#baba.append(iki)
		#print(a)
		# newlist = sorted(a, key=lambda k: (k['durum'][0],k['durum'][1]))
		#a = [{'name':"Beşiktaş","durum":[1,1,3]},{'name':"Galatasaray","durum":[1,0,3]},{'name':"Fener","durum":[1,2,3]}]
	tum_neticeler.append(ev_sahibi_neticeler)
	tum_neticeler.append(deplesman_neticeler)
	return tum_neticeler

def takim_hafta_puan(*args):
	hepsi=[0,0,0,0,0,0,0,0,
		   0,0,0,0,0,0,0,0,
		   0,0,0,0,0,0,0,0]
	for a in args:
		#print(a)
		hepsi = map(add,hepsi,a)
	return list(hepsi)
	

def sirala(liste):
	newlist = sorted(liste, key=lambda k: (k[0]['durum'][7],k[0]['durum'][6]))
	return newlist