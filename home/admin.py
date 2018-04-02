from django.contrib import admin
from .models import SosyalMedia,Yorum,Karakterler,TV,Yazi,Yazarlar,Konu,Puan
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
	search_fields = ['isim','content']
	list_editable = ['content1',]#buraya verdiğimiz alanlar link halinde olmamalı.
	class Meta:
		model = SosyalMedia

admin.site.register(SosyalMedia,SosyalAdmin)
admin.site.register(Puan,PuanAdmin)
admin.site.register(Yorum)
admin.site.register(Karakterler)
admin.site.register(TV)
admin.site.register(Yazi)
admin.site.register(Yazarlar)
admin.site.register(Konu)
