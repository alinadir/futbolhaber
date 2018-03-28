from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Haberler(models.Model):
	title = models.CharField(max_length=120,verbose_name="Başlık")
	content = models.TextField(verbose_name="içerik")
	publishing_date = models.DateTimeField(verbose_name="yayımlanma_tarihi",auto_now_add=True)
	image = models.ImageField(null=True, blank=True)#kullanabilmek için Pillow yüklemek gerekiyor.
	#slug = models.SlugField(unique=True, editable=False,max_length=130 )
	slug = models.SlugField(unique=True, editable=False,max_length=130 )
	haberin_konusu = models.CharField(max_length=20,verbose_name="Haberin Konusu")
	haberin_kaynagı = models.CharField(max_length=30,verbose_name="Haberin Kaynağı")
	haberin_ozeti = models.CharField(max_length=120,verbose_name="Haberin Özeti ")
	
	
	def __str__(self):#bu metot admin paneline eklediğimiz postların title adında gözükmesini sağlıyor.
		return self.title
		
	def get_absolute_url(self):
		return reverse('homee:detail',kwargs={'slug':self.slug})
		# detail url içerisinde name.e verdiğimiz isim. id ise url.de tanımlanan argüman.
		#burdaki home url dosyası içerisinde belirlediğimiz app_name.dir.
		
	class Meta:
		ordering = ['-publishing_date']
	
	def get_unique_slug(self):
		slug = slugify(self.title.replace('ı','i'))
		unique_slug = slug
		counter = 1
		
		while Haberler.objects.filter(slug = unique_slug).exists():
			unique_slug = '{}-{}'.format(slug,counter)
			counter  += 1
		return unique_slug
	
	def save(self,*args,**kwargs):
		#if not self.slug:
		self.slug = self.get_unique_slug()
		return super(Haberler,self).save(*args,*kwargs)
		
class Karakterler(models.Model):
	isim = models.CharField(max_length=40,verbose_name="İsim Soyisim")
	image = models.ImageField()
	
	def __str__(self):#bu metot admin paneline eklediğimiz postların title adında gözükmesini sağlıyor.
		return self.isim
	
		
class SosyalMedia(models.Model):
	isim = models.ForeignKey(Karakterler, related_name="karakter",on_delete=models.CASCADE)
	content1 = models.CharField(max_length=300,verbose_name="media içeriği")
	content2 = models.TextField(verbose_name="içerik")
	konu = models.CharField(max_length=40,verbose_name="konu")
	#image = models.ImageField(null=True, blank=True)
	slug = models.SlugField(unique=True, editable=False,max_length=130)
	publishing_date = models.DateTimeField(verbose_name="yayımlanma_tarihi",auto_now_add=True)
	
	
	
	def __str__(self):#bu metot admin paneline eklediğimiz postların title adında gözükmesini sağlıyor.
		return self.isim.isim
		
	def get_absolute_url(self):
		return reverse('homee:sdetail',kwargs={'slug':self.slug})
	
	class Meta:
		ordering = ['-publishing_date']
	
	def get_unique_slug(self):
		slug = slugify(self.isim.isim.replace('ı','i'))
		unique_slug = slug
		counter = 1
		
		while SosyalMedia.objects.filter(slug = unique_slug).exists():
			unique_slug = '{}-{}'.format(slug,counter)
			counter  += 1
		return unique_slug
	
	def save(self,*args,**kwargs):
		#if not self.slug:
		self.slug = self.get_unique_slug()
		return super(SosyalMedia,self).save(*args,*kwargs)

class Comment(models.Model):
	post = models.ForeignKey(SosyalMedia, related_name="comments",on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	content=models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):#bu metot admin paneline eklediğimiz postların title adında gözükmesini sağlıyor.
		return self.name
	
	def get_unique_name(self):
		name=self.name
		unique_name = self.name
		counter = 1
		
		while Comment.objects.filter(name = unique_name).exists():
			unique_name = '{}-{}'.format(name,counter)
			counter  += 1
		return unique_name
	
	def save(self,*args,**kwargs):
		#if not self.slug:
		self.name = self.get_unique_name()
		return super(Comment,self).save(*args,*kwargs)

		
class Club(models.Model):
	sözluk = {}
	isim = models.CharField(max_length=200)
	image = models.ImageField(blank=True)
	
	oynadıgı_mac = models.IntegerField(default=0,verbose_name="Oynadığı Maç Sayısı")
	galibiyet = models.IntegerField(default=0,verbose_name="Galibiyet")
	beraberlik = models.IntegerField(default=0,verbose_name="Beraberlik")
	maglubiyet = models.IntegerField(default=0,verbose_name="Mağlubiyet")
	atılan_gol = models.IntegerField(default=0,verbose_name="Attığı Gol")
	yenilen_gol = models.IntegerField(default=0,verbose_name="Yediği Gol")
	averaj = models.IntegerField(default=0,verbose_name="Averaj")
	puan = models.IntegerField(default=0,blank=True,verbose_name="Puan")
	
	class Meta:
		ordering = ['-puan','-averaj']
	
	#def hafta_puan_hesapla(self,hafta):
	
		#if hafta=='birinci':
		#	bir = {'puan':self.puan}
		#	sözlük = {}
		#	sözlük[hafta]=bir
		#	print(sözlük)
		#else:
		#	sözlük[hafta]=self.puan
		#	print(sözlük)
		#print(self.sözlük)
		#return self.sözlük
	
	
	def __str__(self):#bu metot admin paneline eklediğimiz postların title adında gözükmesini sağlıyor.
		return self.isim

class Hafta (models.Model):
	kacıncı_hafta = models.CharField("Hangi hafta",max_length=200)
	
	class Meta:
		ordering = ['kacıncı_hafta']
	
	def __str__(self):#bu metot admin paneline eklediğimiz postların title adında gözükmesini sağlıyor.
		return self.kacıncı_hafta
		
class Fikstur(models.Model):
	takım1 = models.ForeignKey(Club, on_delete=models.CASCADE,verbose_name="Takım1",related_name="evsahibi")
	takım2 = models.ForeignKey(Club, on_delete=models.CASCADE,verbose_name="Takım2",related_name="konuktakım")
	takım1_skor= models.IntegerField(default=0,verbose_name="Takım1 skor")
	takım2_skor= models.IntegerField(default=0,verbose_name="Takım2 skor")
	mac_saati = models.DateTimeField("Maç saati",blank=True)
	hafta = models.ForeignKey(Hafta, on_delete=models.CASCADE,verbose_name="Kaçıncı Hafta olduğu")
	macın_durumu=models.CharField(max_length=200,default="baslamadı")
	kontrol=models.IntegerField(default=0,verbose_name="ikinci kez kontrol etme ")
	
	class Meta:
		ordering = ['-mac_saati']
	
	def __str__(self):#bu metot admin paneline eklediğimiz postların title adında gözükmesini sağlıyor.
		return self.hafta.kacıncı_hafta + " " + self.takım1.isim + "-" +self.takım2.isim
	
	def save(self,*args,**kwargs):
		#if not self.slug:
		
		if self.macın_durumu=="bitti" and self.kontrol==0:
			#self.takım1.hafta_puan_hesapla(self.hafta.kacıncı_hafta)
			#self.takım2.hafta_puan_hesapla(self.hafta.kacıncı_hafta)
			self.kontrol += 1
			self.takım1.oynadıgı_mac += 1
			self.takım2.oynadıgı_mac += 1
			self.takım1.averaj +=self.takım1_skor-self.takım2_skor
			self.takım2.averaj +=self.takım2_skor-self.takım1_skor
			self.takım1.atılan_gol += self.takım1_skor
			self.takım2.atılan_gol += self.takım2_skor
			
			if self.takım1_skor > self.takım2_skor:
				self.takım1.puan += 3
				self.takım1.galibiyet += 1
				self.takım2.maglubiyet +=1
			
			if self.takım1_skor < self.takım2_skor:
				self.takım2.puan += 3
				self.takım2.galibiyet += 1
				self.takım1.maglubiyet +=1
				
			if self.takım1_skor == self.takım2_skor:
				self.takım2.puan += 1
				self.takım2.puan += 1
				self.takım2.beraberlik += 1
				self.takım1.beraberlik += 1
			
			self.takım1.save()
			self.takım2.save()
		return super(Fikstur,self).save(*args,*kwargs)

class TV(models.Model):
	programın_adı = models.CharField(max_length=200)
	kanal_adı = models.CharField(max_length=200)
	programın_saati = models.DateTimeField("Maç saati")
	sunucular= models.CharField(max_length=200,blank=True)
	konuklar =models.CharField(max_length=200,blank=True)
	
	def __str__(self):#bu metot admin paneline eklediğimiz postların title adında gözükmesini sağlıyor.
		return self.programın_adı

class Yazarlar(models.Model):

	isim = models.CharField(max_length=200)
	def __str__(self):#bu metot admin paneline eklediğimiz postların title adında gözükmesini sağlıyor.
		return self.isim
		
class Yazi(models.Model):
	
	yazar = models.ForeignKey(Yazarlar, on_delete=models.CASCADE,verbose_name="yazar",related_name="yazar")
	yazının_baslıgı = models.CharField(max_length=200)
	ilgi = models.CharField(max_length=200)
	ana_content=models.TextField()
	ara_baslık1 = models.CharField(max_length=200)
	ara_content1=models.TextField()
	ara_baslık2 = models.CharField(max_length=200)
	ara_content2=models.TextField()
	ara_baslık3 =models.CharField(max_length=200) 
	ara_content3=models.TextField()
	ara_baslık4 =models.CharField(max_length=200)
	ara_content4=models.TextField()
	
	
	def __str__(self):#bu metot admin paneline eklediğimiz postların title adında gözükmesini sağlıyor.
		return self.yazının_baslıgı
	





































	