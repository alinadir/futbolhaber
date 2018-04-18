from django.contrib import admin
from .models import SosyalMedia,Yorum,Karakterler,Yazi,Yazarlar,Konu,Puan
from django.utils.text import slugify

# Register your models here.
class PuanAdmin(admin.ModelAdmin):
	
	list_display = ['isim','puan','averaj']
	list_display_links = ['isim']
	list_filter = ['puan','averaj']
	search_fields = ['isim']
	list_editable = ['puan','averaj',]#buraya verdiğimiz alanlar link halinde olmamalı.
	class Meta:
		model = Puan

class SosyalAdmin(admin.ModelAdmin):
	
	list_display = ['isim','content1']
	list_display_links = ['isim']
	list_filter = ['publishing_date']
	search_fields = ['isim','content1','content2']
	list_editable = ['content1',]#buraya verdiğimiz alanlar link halinde olmamalı.
	class Meta:
		model = SosyalMedia

class YazıAdmin(admin.ModelAdmin):
	
	list_display = ['yazar','yazının_baslıgı']
	list_display_links = ['yazar']
	list_filter = ['yazar']
	search_fields = ['ana_content','yazar','yazının_baslıgı']
	list_editable = ['yazının_baslıgı',]#buraya verdiğimiz alanlar link halinde olmamalı.
	class Meta:
		model = Yazi

class YorumAdmin(admin.ModelAdmin):
	
	list_display = ['isim','yorumunuz']
	list_display_links = ['isim']
	list_filter = ['isim']
	search_fields = ['isim','yorumunuz',]
	list_editable = ['yorumunuz',]#buraya verdiğimiz alanlar link halinde olmamalı.
	class Meta:
		model = Yorum


admin.site.register(SosyalMedia,SosyalAdmin)
admin.site.register(Puan,PuanAdmin)
admin.site.register(Yazi,YazıAdmin)
admin.site.register(Yorum,YorumAdmin)
admin.site.register(Karakterler)
admin.site.register(Yazarlar)
admin.site.register(Konu)

