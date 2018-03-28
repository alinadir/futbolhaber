from django.db import models

# Create your models here.

class Takım(models.Model):
	takım = models.CharField(max_length=20)
	def __str__(self):#bu metot admin paneline eklediğimiz postların title adında gözükmesini sağlıyor.
		return self.takım
		
		
class Hafta(models.Model):
	hafta = models.IntegerField(verbose_name="Hafta") 
	sezon = models.CharField(max_length=20)
	def __str__(self):#bu metot admin paneline eklediğimiz postların title adında gözükmesini sağlıyor.
		return str(self.hafta)
	
class Puan(models.Model):
	hafta = models.ForeignKey(Hafta, on_delete=models.CASCADE)
	takım = models.ForeignKey(Takım, on_delete=models.CASCADE)
	lig= models.CharField(max_length=40,verbose_name="Ligin adı")
	haftaa= models.IntegerField(verbose_name="Kaçıncı hafta")
	o = models.IntegerField(default=0,verbose_name="Oynadığı Maç Sayısı")
	g = models.IntegerField(default=0,verbose_name="Galibiyet")
	b = models.IntegerField(default=0,verbose_name="Beraberlik")
	m = models.IntegerField(default=0,verbose_name="Mağlubiyet")
	a = models.IntegerField(default=0,verbose_name="Attığı Gol")
	y = models.IntegerField(default=0,verbose_name="Yediği Gol")
	avg = models.IntegerField(default=0,verbose_name="Averaj")
	p = models.IntegerField(default=0,blank=True,verbose_name="Puan")
	publishing_date = models.DateTimeField(verbose_name="yayımlanma_tarihi",auto_now_add=True)
	
	def __str__(self):#bu metot admin paneline eklediğimiz postların title adında gözükmesini sağlıyor.
		return str(self.takım) + "" +str(self.hafta) 
	
	class Meta:
		ordering = ['lig','-haftaa','-p','-avg']	
	
	
class Fiks(models.Model):
	hafta = models.ForeignKey(Hafta, on_delete=models.CASCADE)
	haftaa= models.IntegerField(verbose_name="Kaçıncı hafta")
	lig= models.CharField(max_length=40,verbose_name="Ligin adı")
	
	takım1= models.ForeignKey(Takım, related_name="takım1",on_delete=models.CASCADE)
	takım2= models.ForeignKey(Takım,related_name="takım2", on_delete=models.CASCADE)
	takım1_skor= models.IntegerField(null=True,blank=True,verbose_name="takım1 skor")
	takım2_skor= models.IntegerField(null=True,blank=True,verbose_name="takım2 skor")
	macın_tarihi1= models.DateTimeField(null=True,blank=True,verbose_name="maçın tarihi ve saati")
	
	takım3= models.ForeignKey(Takım, related_name="takım3",on_delete=models.CASCADE)
	takım4= models.ForeignKey(Takım,related_name="takım4", on_delete=models.CASCADE)
	takım3_skor= models.IntegerField(null=True,blank=True,verbose_name="takım1 skor")
	takım4_skor= models.IntegerField(null=True,blank=True,verbose_name="takım2 skor")
	macın_tarihi2= models.DateTimeField(null=True,blank=True,verbose_name="maçın tarihi ve saati")
	
	
	
	
	publishing_date = models.DateTimeField(verbose_name="yayımlanma_tarihi",auto_now_add=True)

	class Meta:
		ordering = ['lig','-haftaa','lig']
	

	
	def __str__(self):#bu metot admin paneline eklediğimiz postların title adında gözükmesini sağlıyor.
		return str(self.hafta)
		
	def puan_hesapla(self,takım1,takım2):
		
			if takım1==takım2:
				return [1, 1,0,0,1,1,0,0]
			if takım1>takım2:
				return [3, 0,1,0,0,0,0,1]
			if takım2>takım1:
				return [0, 3,0,1,0,0,1,0]
				
	def ilk_hafta(self,takım1,takım2,skorlar):
		takım1.o = self.haftaa
		takım1.p = skorlar[0]
		takım1.g = skorlar[2]
		takım1.b = skorlar[4]
		takım1.m = skorlar[6]
		
		
		takım2.o = self.haftaa
		takım2.p = skorlar[1]
		takım2.g = skorlar[3]
		takım2.b = skorlar[5]
		takım2.m = skorlar[7]
		takım1.save()
		takım2.save()
	
	def sonraki_hafta(self,takım1,takım2,skorlar,ag,yg):
		takım11=Puan.objects.get(takım=takım1.takım,haftaa=self.haftaa-1)
		takım22=Puan.objects.get(takım=takım2.takım,haftaa=self.haftaa-1)
		
		takım1.g = skorlar[2] + takım11.g
		takım1.b = skorlar[4] + takım11.b
		takım1.m = skorlar[6] + takım11.m
		
		takım2.g = skorlar[3] + takım22.g
		takım2.b = skorlar[5] + takım22.b
		takım2.m = skorlar[7] + takım22.m
		
		takım1.o = self.haftaa
		takım1.p = skorlar[0] + takım11.p
		takım2.o = self.haftaa
		takım2.p = skorlar[1] + takım22.p
		
		takım1.a=ag + takım11.a
		takım1.y=yg + takım11.y
		takım2.a=yg + takım22.a
		takım2.y=ag + takım22.y
		takım1.avg =ag-yg + takım11.avg
		takım2.avg =yg-ag +takım22.avg
		takım1.save()
		takım2.save()
		
	def sonraki_hafta0(self,takım1,takım2):
		takım11=Puan.objects.get(takım=takım1.takım,haftaa=self.haftaa-1)
		takım22=Puan.objects.get(takım=takım2.takım,haftaa=self.haftaa-1)
		
		takım1.g = takım11.g
		takım1.b = takım11.b
		takım1.m = takım11.m
		
		takım2.g = takım22.g
		takım2.b = takım22.b
		takım2.m = takım22.m
		
		takım1.o = self.haftaa-1
		takım1.p = takım11.p
		takım2.o = self.haftaa-1
		takım2.p = takım22.p
		
		takım1.a=takım11.a
		takım1.y=takım11.y
		takım2.a=takım22.a
		takım2.y=takım22.y
		takım1.avg =takım11.avg
		takım2.avg =takım22.avg
		takım1.save()
		takım2.save()
		
	
	
	def save(self,*args,**kwargs):
		if self.takım1_skor:
			takım1=Puan.objects.get(takım=self.takım1,hafta=self.hafta)
			takım2=Puan.objects.get(takım=self.takım2,hafta=self.hafta)
			
			skorlar = self.puan_hesapla(self.takım1_skor,self.takım2_skor)
			if self.haftaa==1:
				
				takım1.a=self.takım1_skor
				takım1.y=self.takım2_skor
				takım2.a=self.takım2_skor
				takım2.y=self.takım1_skor
				takım1.avg =self.takım1_skor-self.takım2_skor
				takım2.avg =self.takım2_skor-self.takım1_skor
				self.ilk_hafta(takım1,takım2,skorlar)
			else:
				self.sonraki_hafta(takım1,takım2,skorlar,self.takım1_skor,self.takım2_skor)
		else:
			takım1=Puan.objects.get(takım=self.takım1,hafta=self.hafta)
			takım2=Puan.objects.get(takım=self.takım2,hafta=self.hafta)
			if self.haftaa==1:
				pass
			else:	
				self.sonraki_hafta0(takım1,takım2)
				
		if self.takım3_skor:
			takım3=Puan.objects.get(takım=self.takım3,hafta=self.hafta)
			takım4=Puan.objects.get(takım=self.takım4,hafta=self.hafta)
			skorlar = self.puan_hesapla(self.takım3_skor,self.takım4_skor)
			if self.haftaa==1:
				takım3.a=self.takım3_skor
				takım3.y=self.takım4_skor
				takım4.a=self.takım4_skor
				takım4.y=self.takım3_skor
				takım3.avg =self.takım3_skor-self.takım4_skor
				takım4.avg =self.takım4_skor-self.takım3_skor
				self.ilk_hafta(takım3,takım4,skorlar)
			else:
				self.sonraki_hafta(takım3,takım4,skorlar,self.takım3_skor,self.takım4_skor)
		else:
			takım3=Puan.objects.get(takım=self.takım3,hafta=self.hafta)
			takım4=Puan.objects.get(takım=self.takım4,hafta=self.hafta)
			if self.haftaa==1:
				pass
			else:	
				self.sonraki_hafta0(takım3,takım4)
				
				
		#takım3=Puan.objects.get(takım=self.takım1,hafta=self.haftaa+1)
		#takım4=Puan.objects.get(takım=self.takım2,hafta=self.haftaa+1)
		#skorlar = self.puan_hesapla(self.takım1_skor,self.takım2_skor)
		#takım1.p = takım1.p+skorlar[0]		
		#takım1.save()
		#3takım2.p = takım2.p+skorlar[1]
		#takım2.save()
		#takım3.p = takım1.p
		#takım4.p = takım2.p
		#takım3.save()
	#	#takım4.save()
	#	print(skorlar)
	#	print(takım1.p)
	#	print(takım2.p)
		return super(Fiks,self).save(*args,*kwargs)
		
class PremierPuan(Puan):
	pass
class PremierFiks(Fiks):
	pass
class PremierTakım(Takım):
	pass
class PremierHafta(Hafta):
	pass