from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Klup(models.Model):
	isim = models.CharField(max_length=200)
	image = models.ImageField(blank=True)
	puan = models.IntegerField(default=0,blank=True,verbose_name="Puan")
	averaj = models.IntegerField(default=0,blank=True,verbose_name="Averaj")
	
	class Meta:
		ordering = ['-puan','-averaj']
	
	def __str__(self):#bu metot admin paneline eklediğimiz postların title adında gözükmesini sağlıyor.
		return self.isim

class Hafta (models.Model):
	kacıncı_hafta = models.CharField("Hangi hafta",max_length=200)
	
	
	class Meta:
		ordering = ['kacıncı_hafta']
	
	def __str__(self):#bu metot admin paneline eklediğimiz postların title adında gözükmesini sağlıyor.
		return self.kacıncı_hafta

		
class Fikstur(models.Model):
	takım1 = models.ForeignKey(Klup, on_delete=models.CASCADE,verbose_name="Takım1",related_name="evsahibi")
	takım2 = models.ForeignKey(Klup, on_delete=models.CASCADE,verbose_name="Takım2",related_name="konuktakım")
	takım1_skor= models.IntegerField(default=0,verbose_name="Takım1 skor")
	takım2_skor= models.IntegerField(default=0,verbose_name="Takım2 skor")
	mac_saati = models.DateTimeField("Maç saati",auto_now=False)
	hafta = models.ForeignKey(Hafta, on_delete=models.CASCADE,verbose_name="Kaçıncı Hafta olduğu")
	macın_durumu=models.CharField(max_length=200,default="baslamadı")
	kontrol=models.IntegerField(default=0,verbose_name="ikinci kez kontrol etme ")
	sezon =  models.CharField("Sezon",max_length=200,default="2017/2018")
	hakem = models.CharField("Hakem",max_length=50,default="-")
	yardımcı_hakemler = models.CharField("Yan Hakemler",max_length=200,default="-")
	stadyum = models.CharField("Stadyum",max_length=50,default="-")
	
	goller1 = models.CharField("Goller1",max_length=300,default="-")	
	sarıkartlar1 =models.CharField("Sarı Kartlar1",max_length=200,default="-")
	kırmızıkartlar1 = models.CharField("Kırmızı Kartlar1",max_length=200,default="-")
	
	goller2 = models.CharField("Goller2",max_length=300,default="-")	
	sarıkartlar2 =models.CharField("Sarı Kartlar2",max_length=200,default="-")
	kırmızıkartlar2 = models.CharField("Kırmızı Kartlar2",max_length=200,default="-")
	
	ilkonbir1 = models.CharField("ilkonbirler1",max_length=400,default="-")
	ilkonbir2 =models.CharField("ilkonbirler1",max_length=400,default="-")
	
	giren_oyuncular1=models.CharField("Girenler1",max_length=200,default="-")
	giren_oyuncular2=models.CharField("Girenler2",max_length=200,default="-")
	
	cıkan_oyuncular1=models.CharField("Çıkanlar1",max_length=200,default="-")
	cıkan_oyuncular2=models.CharField("Çıkanlar2",max_length=200,default="-")
	
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
	

	
	oynadıgı_mac2 = models.IntegerField(default=0,verbose_name="Oynadığı Maç Sayısı")
	galibiyet2 = models.IntegerField(default=0,verbose_name="Galibiyet")
	beraberlik2 = models.IntegerField(default=0,verbose_name="Beraberlik")
	maglubiyet2 = models.IntegerField(default=0,verbose_name="Mağlubiyet")
	averaj2 = models.IntegerField(default=0,verbose_name="Averaj")
	puan2 = models.IntegerField(default=0,blank=True,verbose_name="Puan")

	

	
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
			
			
			if self.takım1_skor > self.takım2_skor:
				self.puan1 = 3
				self.galibiyet1 = 1
				self.maglubiyet2 =1
				
			
			if self.takım1_skor < self.takım2_skor:
				self.puan2 = 3
				self.galibiyet2 = 1
				self.maglubiyet1 =1
				
				
			if self.takım1_skor == self.takım2_skor:
				self.puan1 = 1
				self.puan2 = 1
				self.beraberlik2 = 1
				self.beraberlik1 = 1
					
		return super(Fikstur,self).save(*args,*kwargs)
			
			
		
	
	
	class Meta:
		ordering = ['-mac_saati']
	
	def __str__(self):#bu metot admin paneline eklediğimiz postların title adında gözükmesini sağlıyor.
		return self.hafta.kacıncı_hafta + ".Hafta" + " " + self.takım1.isim + "-" +self.takım2.isim

class Oyuncu(models.Model):
	isim = models.CharField(max_length=200)
	takım =models.ForeignKey(Klup, on_delete=models.CASCADE,verbose_name="Takım",related_name="Takımgol")
	
	mac_sayısı = models.IntegerField(default=0,blank=True,verbose_name="Maç sayısı")
	asist_sayısı = models.IntegerField(default=0,blank=True,verbose_name="Asist sayısı")
	gol_sayısı = models.IntegerField(default=0,blank=True,verbose_name="Gol sayısı")
	sarıkart_sayısı = models.IntegerField(default=0,blank=True,verbose_name="Sarıkart sayısı")
	kırmızı_sayısı = models.IntegerField(default=0,blank=True,verbose_name="Kırmızı Kart sayısı")

	dogum_tarihi=models.DateTimeField(verbose_name="Doğum Tarihi",auto_now=True)
	yaş = models.IntegerField(verbose_name="Yaş",default=0)
	deger = models.CharField(max_length=20,blank=True)
	ülke = models.CharField(max_length=20,blank=True)
	maas = models.CharField(max_length=20,blank=True)
	sözlesme_baslangıc_tarihi = models.DateTimeField(verbose_name="Sözleşme Başlangıç Tarihi",auto_now=True)
	sözlesme_bitiş_tarihi = models.DateTimeField(verbose_name="Sözleşme Bitiş Tarihi",auto_now=True)
	def __str__(self):
		return self.isim



		





	