from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Karakterler(models.Model):
	isim = models.CharField(max_length=40,verbose_name="İsim Soyisim")
	image = models.ImageField()
	ozgecmis = models.CharField(max_length=500,verbose_name="özgeçmiş",null=True,blank = True)
	
	def __str__(self):#bu metot admin paneline eklediğimiz postların title adında gözükmesini sağlıyor.
		return self.isim
		
class Konu(models.Model):
	isim = models.CharField(max_length=40,verbose_name="Örnek:Beşiktaş,Genel,Dünya,Anadolu")
	def __str__(self):
		return self.isim
			
class SosyalMedia(models.Model):
	isim = models.ForeignKey(Karakterler, on_delete=models.CASCADE,related_name="Karakterler")
	content1 = models.CharField(max_length=300,verbose_name="media içeriği")
	content2 = models.TextField()
	konu = models.ForeignKey(Konu,on_delete=models.CASCADE,related_name="Konu")
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
		slug = slugify(self.content1.replace('ı','i'))
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

class Yorum(models.Model):
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
		
		while Yorum.objects.filter(name = unique_name).exists():
			unique_name = '{}-{}'.format(name,counter)
			counter  += 1
		return unique_name
	
	def save(self,*args,**kwargs):
		#if not self.slug:
		self.name = self.get_unique_name()
		return super(Yorum,self).save(*args,*kwargs)

class TV(models.Model):
	programın_adı = models.CharField(max_length=200)
	kanal_adı = models.CharField(max_length=200)
	programın_saati = models.DateTimeField("Maç saati")
	sunucular= models.CharField(max_length=200,blank=True,null=True)
	konuklar =models.CharField(max_length=200,blank=True,null=True)
	
	def __str__(self):#bu metot admin paneline eklediğimiz postların title adında gözükmesini sağlıyor.
		return self.programın_adı

class Yazarlar(models.Model):

	isim = models.CharField(max_length=200)
	def __str__(self):#bu metot admin paneline eklediğimiz postların title adında gözükmesini sağlıyor.
		return self.isim
		
class Yazi(models.Model):
	
	yazar = models.ForeignKey(Yazarlar, on_delete=models.CASCADE,verbose_name="yazar",related_name="yazar")
	yazının_baslıgı = models.CharField(max_length=200)
	konu = models.ForeignKey(Konu,on_delete=models.CASCADE,related_name="İlgi")
	ana_content=models.TextField()
	
	def __str__(self):#bu metot admin paneline eklediğimiz postların title adında gözükmesini sağlıyor.
		return self.yazar.isim + " " + self.yazının_baslıgı
	





































	