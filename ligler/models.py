from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Ülke(models.Model):
	isim = models.CharField(max_length=100)
	def __str__(self):
		return self.isim

class Hakemler(models.Model):
	isim = models.CharField(max_length=100)
	def __str__(self):
		return self.isim
		
class Yardımcılar(models.Model):
	isim = models.CharField(max_length=100)
	dogum_tarihi=models.DateTimeField(verbose_name="Doğum Tarihi",auto_now=True)
	yaş = models.IntegerField(verbose_name="Yaş",blank=True,null=True)
	millet = models.ForeignKey(Ülke, on_delete=models.CASCADE)
	def __str__(self):
		return self.isim

		
class Hoca(models.Model):
	isim = models.CharField(max_length=100)
	c=models.CharField(max_length=100)
	dogum_tarihi=models.DateTimeField(verbose_name="Doğum Tarihi",auto_now=True)
	yaş = models.IntegerField(verbose_name="Yaş",blank=True,null=True)
	ülke = models.ForeignKey(Ülke, on_delete=models.CASCADE)
	maas = models.CharField(max_length=20,blank=True,null=True)
	sözlesme_baslangıc_tarihi = models.DateTimeField(verbose_name="Sözleşme Başlangıç Tarihi",auto_now=True)
	sözlesme_bitiş_tarihi = models.DateTimeField(verbose_name="Sözleşme Bitiş Tarihi",auto_now=True)
	toplam_maç_sayısı = models.IntegerField(verbose_name="Maç sayısı",blank=True,null=True)
	toplam_gol_sayısı = models.IntegerField(verbose_name="Gol sayısı",blank=True,null=True)
	toplam_asist_sayısı = models.IntegerField(verbose_name="Asist sayısı",blank=True,null=True)
	toplam_sarıkart_sayısı = models.IntegerField(verbose_name="Sarı Kart sayısı",blank=True,null=True)
	toplam_kırmızı_sayısı = models.IntegerField(verbose_name="Kırmızı Kart sayısı",blank=True,null=True)
	yardımcılar = models.ManyToManyField('Yardımcılar')
	calsıtırdıgı_takımlar = models.CharField(max_length=300)
	
	def __str__(self):#bu metot admin paneline eklediğimiz postların title adında gözükmesini sağlıyor.
		return self.isim

class Yoneticiler(models.Model):
	baskan =  models.CharField(max_length=100)
	yöneticiler =  models.CharField(max_length=500)
	def __str__(self):
		return self.baskan
		
class Stadyum(models.Model):
	isim =  models.CharField(max_length=50)
	kapasite =  models.CharField(max_length=50)
	def __str__(self):
		return self.isim

class İdman(models.Model):
	isim =  models.CharField(max_length=50)
	
	def __str__(self):
		return self.isim

		
class Takım(models.Model):
	isim = models.CharField(max_length=100)
	kurulus_tarihi=models.DateTimeField(verbose_name="Doğum Tarihi",auto_now=True)
	ülke = models.ForeignKey(Ülke, on_delete=models.CASCADE)
	yoneticiler = models.ManyToManyField('Yoneticiler',related_name="yoneticiler")
	hoca = models.ManyToManyField('Hoca',related_name="hoca")
	stadyum = models.ForeignKey(Stadyum, on_delete=models.CASCADE,related_name="stadyum")
	idman_yeri = models.ForeignKey(İdman, on_delete=models.CASCADE,related_name="idman")
	
	oynadıgı_mac = models.IntegerField(default=0,verbose_name="Oynadığı Maç Sayısı")
	galibiyet = models.IntegerField(default=0,verbose_name="Galibiyet")
	beraberlik = models.IntegerField(default=0,verbose_name="Beraberlik")
	maglubiyet = models.IntegerField(default=0,verbose_name="Mağlubiyet")
	atılan_gol = models.IntegerField(default=0,verbose_name="Attığı Gol")
	yenilen_gol = models.IntegerField(default=0,verbose_name="Yediği Gol")
	averaj = models.IntegerField(default=0,verbose_name="Averaj")
	puan = models.IntegerField(default=0,verbose_name="Puan")
	def __str__(self):
		return self.isim

class Oyuncu(models.Model):
	isim = models.CharField(max_length=100)
	toplam_maç_sayısı = models.IntegerField(default=0,verbose_name="Maç sayısı",blank=True)
	toplam_gol_sayısı = models.IntegerField(default=0,verbose_name="Gol sayısı",blank=True)
	toplam_asist_sayısı = models.IntegerField(default=0,verbose_name="Asist sayısı",blank=True)
	toplam_sarıkart_sayısı = models.IntegerField(default=0,verbose_name="Sarı Kart sayısı",blank=True)
	toplam_kırmızı_sayısı = models.IntegerField(default=0,verbose_name="Kırmızı Kart sayısı",blank=True)
	toplam_onbir_sayısı = models.IntegerField(default=0,verbose_name="Onbir çıktığı maç sayısı")
	takımı =  models.ForeignKey(Takım, on_delete=models.CASCADE)
	
	
	dogum_tarihi=models.DateTimeField(verbose_name="Doğum Tarihi",auto_now=True)
	yaş = models.IntegerField(verbose_name="Yaş",blank=True,null=True)
	deger = models.CharField(max_length=20,blank=True,null=True)
	ülke = models.ForeignKey(Ülke, on_delete=models.CASCADE)
	maas = models.CharField(max_length=20,blank=True,null=True)
	sözlesme_baslangıc_tarihi = models.DateTimeField(verbose_name="Sözleşme Başlangıç Tarihi",auto_now=True)
	sözlesme_bitiş_tarihi = models.DateTimeField(verbose_name="Sözleşme Bitiş Tarihi",auto_now=True)

	menajer = models.CharField(max_length=100,blank=True,null=True)
	def __str__(self):#bu metot admin paneline eklediğimiz postların title adında gözükmesini sağlıyor.
		return self.isim

		
class Sezon(models.Model):
	isim =  models.CharField(max_length=50)
	
	def __str__(self):
		return self.isim		
		
class LigKupa(models.Model):
	isim =  models.CharField(max_length=50)
	takımlar = models.ManyToManyField('Takım')
	sezon =  models.ForeignKey(Sezon, on_delete=models.CASCADE)
	def __str__(self):
		return self.isim	

class Hafta (models.Model):
	kacıncı_hafta = models.CharField("Hangi hafta",max_length=200)
	
	
	class Meta:
		ordering = ['kacıncı_hafta']
	
	def __str__(self):#bu metot admin paneline eklediğimiz postların title adında gözükmesini sağlıyor.
		return self.kacıncı_hafta
		
class Fikstur(models.Model):
	takım1 = models.ForeignKey(Takım, on_delete=models.CASCADE,verbose_name="Takım1",related_name="evsahibi")
	takım2 = models.ForeignKey(Takım, on_delete=models.CASCADE,verbose_name="Takım2",related_name="konuktakım")
	takım1_skor= models.IntegerField(default=0,verbose_name="Takım1 skor")
	takım2_skor= models.IntegerField(default=0,verbose_name="Takım2 skor")
	mac_saati = models.DateTimeField("Maç saati",auto_now=False)
	hafta = models.ForeignKey(Hafta, on_delete=models.CASCADE,verbose_name="Kaçıncı Hafta olduğu")
	macın_durumu=models.CharField(max_length=200,default="baslamadı")
	kontrol=models.IntegerField(default=0,verbose_name="ikinci kez kontrol etme ")
	sezon =  models.ForeignKey(Sezon, on_delete=models.CASCADE)
	macın_türü= models.ForeignKey(LigKupa, on_delete=models.CASCADE)
	hakem = models.ForeignKey(Hakemler, on_delete=models.CASCADE,related_name="hakem")
	yardımcı_hakemler = models.ForeignKey(Hakemler, on_delete=models.CASCADE,related_name="yan_hakemler")
	stadyum = models.ForeignKey(Stadyum, on_delete=models.CASCADE,related_name="stad")
	goller1 = models.ManyToManyField(Oyuncu, through='GolEkle1',related_name="goller1")
	asistler1 = models.ManyToManyField(Oyuncu, through='AsistEkle1',related_name="asistler1")
	
	sarıkartlar1 = models.ManyToManyField(Oyuncu, through="SarıEkle1",related_name="sarıkartlar1")
	kırmızıkartlar1 = models.ManyToManyField(Oyuncu,through="KırmızıEkle1", related_name="kırmızılar1")
	
	goller2 = models.ManyToManyField(Oyuncu, through='GolEkle2',related_name="goller2")
	asistler2 = models.ManyToManyField(Oyuncu, through='AsistEkle2',related_name="asistler2")
	
	sarıkartlar2 = models.ManyToManyField(Oyuncu, through="SarıEkle2",related_name="sarıkartlar2")
	kırmızıkartlar2 = models.ManyToManyField(Oyuncu,through="KırmızıEkle2", related_name="kırmızılar2")
	
	ilkonbir1 = models.ManyToManyField(Oyuncu, related_name="ilkonbir1")
	ilkonbir2 = models.ManyToManyField(Oyuncu, related_name="ilkonbir2")
	
	giren_oyuncular1=models.ManyToManyField(Oyuncu,through='Girenler1',related_name="girenler11")
	giren_oyuncular2=models.ManyToManyField(Oyuncu,through='Girenler2', related_name="girenler222")
	
	cıkan_oyuncular1=models.ManyToManyField(Oyuncu, through='Cıkanlar1',related_name="çıkanlar11")
	cıkan_oyuncular2=models.ManyToManyField(Oyuncu, through='Cıkanlar2',related_name="cıkanlar22")
	
	topla_oynama_yüzdesi1 = models.IntegerField(default=0,verbose_name="topla_oynama_yüzdesi1")
	kaleyi_bulan_şut1 = models.IntegerField(default=0,verbose_name="kaleyi_bulan_şut1")
	kaleyi_bulmayan_şut1 = models.IntegerField(default=0,verbose_name="kaleyi_bulmayan_şut1")
	kornerler1 = models.IntegerField(default=0,verbose_name="kornerler1")
	ofsaytlar1 = models.IntegerField(default=0,verbose_name="ofsaytlar1")
	taclar1 = models.IntegerField(default=0,verbose_name="taclar1")
	kaleci_kurtarıslari1 = models.IntegerField(default=0,verbose_name="kaleci_kurtarıslari1")
	fauller1 = models.IntegerField(default=0,verbose_name="fauller1")
	kırmızı_kartlar1 = models.IntegerField(default=0,verbose_name="kırmızı_kartlar1")
	sarı_kartlar1 = models.IntegerField(default=0,verbose_name="sarıkartlar1")
	
	
	topla_oynama_yüzdesi2 = models.IntegerField(default=0,verbose_name="topla_oynama_yüzdesi2")
	kaleyi_bulan_şut2 = models.IntegerField(default=0,verbose_name="kaleyi_bulan_şut2")
	kaleyi_bulmayan_şut2 = models.IntegerField(default=0,verbose_name="kaleyi_bulmayan_şut2")
	kornerler2 = models.IntegerField(default=0,verbose_name="kornerler2")
	ofsaytlar2 = models.IntegerField(default=0,verbose_name="ofsaytlar2")
	kaleci_kurtarıslari2 = models.IntegerField(default=0,verbose_name="kaleci_kurtarıslari2")
	taclar2 = models.IntegerField(default=0,verbose_name="taclar2")
	fauller2 = models.IntegerField(default=0,verbose_name="fauller2")
	kırmızı_kartlar2 = models.IntegerField(default=0,verbose_name="kırmızı_kartlar2")
	sarı_kartlar2 = models.IntegerField(default=0,verbose_name="sarıkartlar2")
	
	oynadıgı_mac1 = models.IntegerField(default=0,verbose_name="Oynadığı Maç Sayısı")
	galibiyet1 = models.IntegerField(default=0,verbose_name="Galibiyet")
	beraberlik1 = models.IntegerField(default=0,verbose_name="Beraberlik")
	maglubiyet1 = models.IntegerField(default=0,verbose_name="Mağlubiyet")
	averaj1 = models.IntegerField(default=0,verbose_name="Averaj")
	puan1 = models.IntegerField(default=0,blank=True,verbose_name="Puan")
	
	#ev_oynadıgı_mac1 = models.IntegerField(default=0,verbose_name="Ev sahibi Oynadığı Maç Sayısı1")
	#ev_galibiyet1 = models.IntegerField(default=0,verbose_name="Galibiyet")
	#ev_beraberlik1 = models.IntegerField(default=0,verbose_name="Beraberlik")
	#ev_maglubiyet1 = models.IntegerField(default=0,verbose_name="Mağlubiyet")
	#ev_averaj1 = models.IntegerField(default=0,verbose_name="Averaj")
	#ev_puan1 = models.IntegerField(default=0,verbose_name="Puan")
	#ev_attıgı_gol1 = models.IntegerField(default=0,verbose_name="Ev sahibi gol sayısı")
	#ev_yedigi_gol1 = models.IntegerField(default=0,verbose_name="Ev sahibi yedigi gol sayısı")
	
	#dep_oynadıgı_mac1 = models.IntegerField(default=0,verbose_name="Deplasman Oynadığı Maç Sayısı1")
	#dep_galibiyet1 = models.IntegerField(default=0,verbose_name="Galibiyet")
	#dep_beraberlik1 = models.IntegerField(default=0,verbose_name="Beraberlik")
	#dep_maglubiyet1 = models.IntegerField(default=0,verbose_name="Mağlubiyet")
	#dep_averaj1 = models.IntegerField(default=0,verbose_name="Averaj")
	#dep_puan1 = models.IntegerField(default=0,verbose_name="Puan")
	#dep_attıgı_gol1 = models.IntegerField(default=0,verbose_name="dep sahibi gol sayısı")
	#dep_yedigi_gol1 = models.IntegerField(default=0,verbose_name="dep sahibi yedigi gol sayısı")
	
	oynadıgı_mac2 = models.IntegerField(default=0,verbose_name="Oynadığı Maç Sayısı")
	galibiyet2 = models.IntegerField(default=0,verbose_name="Galibiyet")
	beraberlik2 = models.IntegerField(default=0,verbose_name="Beraberlik")
	maglubiyet2 = models.IntegerField(default=0,verbose_name="Mağlubiyet")
	averaj2 = models.IntegerField(default=0,verbose_name="Averaj")
	puan2 = models.IntegerField(default=0,blank=True,verbose_name="Puan")

	
	#ev_oynadıgı_mac2 = models.IntegerField(default=0,verbose_name="Ev Oynadığı Maç Sayısı2")
	#ev_galibiyet2 = models.IntegerField(default=0,verbose_name="Galibiyet")
	#ev_beraberlik2 = models.IntegerField(default=0,verbose_name="Beraberlik")
	#ev_maglubiyet2 = models.IntegerField(default=0,verbose_name="Mağlubiyet")
	#ev_averaj2 = models.IntegerField(default=0,verbose_name="Averaj")
	#ev_puan2 = models.IntegerField(default=0,verbose_name="Puan")
	#ev_attıgı_gol2 = models.IntegerField(default=0,verbose_name="Ev sahibi gol sayısı")
	#ev_yedigi_gol2 = models.IntegerField(default=0,verbose_name="Ev sahibi yedigi gol sayısı")
	
	#dep_oynadıgı_mac2 = models.IntegerField(default=0,verbose_name="Deplasman Oynadığı Maç Sayısı2")
	#dep_galibiyet2 = models.IntegerField(default=0,verbose_name="Galibiyet")
	#dep_beraberlik2 = models.IntegerField(default=0,verbose_name="Beraberlik")
	#dep_maglubiyet2 = models.IntegerField(default=0,verbose_name="Mağlubiyet")
	#dep_averaj2 = models.IntegerField(default=0,verbose_name="Averaj")
	#dep_puan2 = models.IntegerField(default=0,verbose_name="Puan")
	#dep_attıgı_gol2 = models.IntegerField(default=0,verbose_name="dep sahibi gol sayısı")
	#dep_yedigi_gol2 = models.IntegerField(default=0,verbose_name="dep sahibi yedigi gol sayısı")
	
	def save(self,*args,**kwargs):
		#if not self.slug:
		
		
		if self.macın_durumu=="bitti" and self.kontrol==0:
			#self.takım1.hafta_puan_hesapla(self.hafta.kacıncı_hafta)
			#self.takım2.hafta_puan_hesapla(self.hafta.kacıncı_hafta)
			#self.kontrol += 1
			self.oynadıgı_mac1 = 1
			self.oynadıgı_mac2 = 1
			self.averaj1 =self.takım1_skor-self.takım2_skor
			self.averaj2 =self.takım2_skor-self.takım1_skor

			self.kontrol = 1
			
			self.takım1.oynadıgı_mac += 1
			self.takım2.oynadıgı_mac += 1
			self.takım1.averaj +=self.takım1_skor-self.takım2_skor
			self.takım2.averaj +=self.takım2_skor-self.takım1_skor
			self.takım1.atılan_gol += self.takım1_skor
			self.takım2.atılan_gol += self.takım2_skor
			self.takım1.yenilen_gol += self.takım2_skor
			self.takım2.yenilen_gol += self.takım1_skor
			
			if self.takım1_skor > self.takım2_skor:
				self.puan1 = 3
				self.galibiyet1 = 1
				self.maglubiyet2 =1
				self.takım1.puan += 3
				self.takım1.galibiyet += 1
				self.takım2.maglubiyet +=1
			
			if self.takım1_skor < self.takım2_skor:
				self.puan2 = 3
				self.galibiyet2 = 1
				self.maglubiyet1 =1
				self.takım2.puan += 3
				self.takım2.galibiyet += 1
				self.takım1.maglubiyet +=1
				
			if self.takım1_skor == self.takım2_skor:
				self.puan1 = 1
				self.puan2 = 1
				self.beraberlik2 = 1
				self.beraberlik1 = 1
				self.takım2.puan += 1
				self.takım1.puan += 1
				self.takım2.beraberlik += 1
				self.takım1.beraberlik += 1
			
		

		

				
			
		self.takım1.save()
		self.takım2.save()
					
		return super(Fikstur,self).save(*args,*kwargs)
			
			
		
	
	
	class Meta:
		ordering = ['-mac_saati']
	
	def __str__(self):#bu metot admin paneline eklediğimiz postların title adında gözükmesini sağlıyor.
		return self.hafta.kacıncı_hafta + " " + self.takım1.isim + "-" +self.takım2.isim
		


class GolEkle1(models.Model):
	futbolcu = models.ForeignKey(Oyuncu,on_delete=models.CASCADE)
	mac = models.ForeignKey(Fikstur,on_delete=models.CASCADE)
	golun_dakikası= models.IntegerField(default=0,verbose_name="Golun dakikası")
	def __str__(self):
		return self.futbolcu.isim + str(self.golun_dakikası)
	def save(self,*args,**kwargs):
		self.futbolcu.toplam_gol_sayısı+=1
		self.futbolcu.save()
		return super(GolEkle1,self).save(*args,*kwargs)

class SarıEkle1(models.Model):
	futbolcu = models.ForeignKey(Oyuncu,on_delete=models.CASCADE)
	mac = models.ForeignKey(Fikstur,on_delete=models.CASCADE)
	sarının_dakikası= models.IntegerField(default=0,verbose_name="sarının dakikası")
	
	def save(self,*args,**kwargs):
		self.futbolcu.toplam_sarıkart_sayısı+=1
		self.futbolcu.save()
		return super(SarıEkle1,self).save(*args,*kwargs)
		
class KırmızıEkle1(models.Model):
	futbolcu = models.ForeignKey(Oyuncu,on_delete=models.CASCADE)
	mac = models.ForeignKey(Fikstur,on_delete=models.CASCADE)
	kırmızının_dakikası= models.IntegerField(default=0,verbose_name="kırmızının dakikası")
	kırmızının_sebebi= models.CharField(max_length=100)
	def save(self,*args,**kwargs):
		self.futbolcu.toplam_kırmızı_sayısı+=1
		self.futbolcu.save()
		return super(KırmızıEkle1,self).save(*args,*kwargs)


class AsistEkle1(models.Model):
	futbolcu = models.ForeignKey(Oyuncu,on_delete=models.CASCADE)
	mac = models.ForeignKey(Fikstur,on_delete=models.CASCADE)
	asistin_dakikası= models.IntegerField(default=0,verbose_name="Golun dakikası")
	def save(self,*args,**kwargs):
		self.futbolcu.toplam_asist_sayısı+=1
		self.futbolcu.save()
		return super(AsistEkle1,self).save(*args,*kwargs)

class Girenler1(models.Model):
	futbolcu = models.ForeignKey(Oyuncu,on_delete=models.CASCADE)
	mac = models.ForeignKey(Fikstur,on_delete=models.CASCADE)
	dakika= models.IntegerField(default=0,verbose_name="Golun dakikası")
	def save(self,*args,**kwargs):
		self.futbolcu.toplam_maç_sayısı+=1
		self.futbolcu.save()
		return super(Girenler1,self).save(*args,*kwargs)

class Cıkanlar1(models.Model):
	futbolcu = models.ForeignKey(Oyuncu,on_delete=models.CASCADE)
	mac = models.ForeignKey(Fikstur,on_delete=models.CASCADE)
	dakika= models.IntegerField(default=0,verbose_name="Golun dakikası")
	
	

class GolEkle2(models.Model):
	futbolcu = models.ForeignKey(Oyuncu,on_delete=models.CASCADE)
	mac = models.ForeignKey(Fikstur,on_delete=models.CASCADE)
	golun_dakikası= models.IntegerField(default=0,verbose_name="Golun dakikası")
	def __str__(self):
		return self.futbolcu.isim + str(self.golun_dakikası)
	def save(self,*args,**kwargs):
		self.futbolcu.toplam_gol_sayısı+=1
		self.futbolcu.save()
		return super(GolEkle2,self).save(*args,*kwargs)

class SarıEkle2(models.Model):
	futbolcu = models.ForeignKey(Oyuncu,on_delete=models.CASCADE)
	mac = models.ForeignKey(Fikstur,on_delete=models.CASCADE)
	sarının_dakikası= models.IntegerField(default=0,verbose_name="sarının dakikası")
	def save(self,*args,**kwargs):
		self.futbolcu.toplam_sarıkart_sayısı+=1
		self.futbolcu.save()
		return super(SarıEkle2,self).save(*args,*kwargs)
	
class KırmızıEkle2(models.Model):
	futbolcu = models.ForeignKey(Oyuncu,on_delete=models.CASCADE)
	mac = models.ForeignKey(Fikstur,on_delete=models.CASCADE)
	kırmızının_dakikası= models.IntegerField(default=0,verbose_name="kırmızının dakikası")
	kırmızının_sebebi= models.CharField(max_length=100)
	def save(self,*args,**kwargs):
		self.futbolcu.toplam_kırmızı_sayısı+=1
		self.futbolcu.save()
		return super(KırmızıEkle2,self).save(*args,*kwargs)
class AsistEkle2(models.Model):
	futbolcu = models.ForeignKey(Oyuncu,on_delete=models.CASCADE)
	mac = models.ForeignKey(Fikstur,on_delete=models.CASCADE)
	asistin_dakikası= models.IntegerField(default=0,verbose_name="Golun dakikası")
	def save(self,*args,**kwargs):
		self.futbolcu.toplam_asist_sayısı+=1
		self.futbolcu.save()
		return super(AsistEkle2,self).save(*args,*kwargs)

class Girenler2(models.Model):
	futbolcu = models.ForeignKey(Oyuncu,on_delete=models.CASCADE)
	mac = models.ForeignKey(Fikstur,on_delete=models.CASCADE)
	dakika= models.IntegerField(default=0,verbose_name="Golun dakikası")
	def save(self,*args,**kwargs):
		self.futbolcu.toplam_maç_sayısı+=1
		self.futbolcu.save()
		return super(Girenler2,self).save(*args,*kwargs)

class Cıkanlar2(models.Model):
	futbolcu = models.ForeignKey(Oyuncu,on_delete=models.CASCADE)
	mac = models.ForeignKey(Fikstur,on_delete=models.CASCADE)
	dakika= models.IntegerField(default=0,verbose_name="Golun dakikası")


	