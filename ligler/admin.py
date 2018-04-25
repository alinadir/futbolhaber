from django.contrib import admin
from .models import Klup,Fikstur,Hafta,Oyuncu

# Register your models here.

class OyuncuAdmin(admin.ModelAdmin):
	
	list_display = ['isim','takım','mac_sayısı','asist_sayısı','gol_sayısı','sarıkart_sayısı','kırmızı_sayısı']
	list_display_links = ['isim']
	list_filter = ['isim','takım','asist_sayısı','gol_sayısı','sarıkart_sayısı','kırmızı_sayısı']
	search_fields = ['isim']
	list_editable = ['mac_sayısı','asist_sayısı','gol_sayısı','sarıkart_sayısı','kırmızı_sayısı',]#buraya verdiğimiz alanlar link halinde olmamalı.
	class Meta:
		model = Oyuncu

class FiksturAdmin(admin.ModelAdmin):
	
	list_display = ['takım1','takım2','takım1_skor','takım2_skor','mac_saati','goller1','sarıkartlar1','kırmızıkartlar1','goller2','sarıkartlar2','kırmızıkartlar2']
	list_display_links = ['takım1','takım2']
	list_filter = ['hafta','takım1','takım2']
	search_fields = ['takım1','takım2','goller1','sarıkartlar1','kırmızıkartlar1','goller2','sarıkartlar2','kırmızıkartlar2']
	list_editable = ['takım1_skor','takım2_skor','mac_saati','goller1','sarıkartlar1','kırmızıkartlar1','goller2','sarıkartlar2','kırmızıkartlar2',]#buraya verdiğimiz alanlar link halinde olmamalı.
	class Meta:
		model = Fikstur

admin.site.register(Oyuncu,OyuncuAdmin)
admin.site.register(Fikstur,FiksturAdmin)
admin.site.register(Klup)
admin.site.register(Hafta)





