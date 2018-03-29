from django.contrib import admin
from .models import SosyalMedia,Comment,Karakterler,Club,Fikstur,Hafta,TV,Yazi,Yazarlar
from django.utils.text import slugify

# Register your models here.
class SosyalAdmin(admin.ModelAdmin):
	
	list_display = ['isim','publishing_date','slug']
	list_display_links = ['publishing_date']
	list_filter = ['publishing_date']
	search_fields = ['isim','content']
	list_editable = ['isim',]#buraya verdiğimiz alanlar link halinde olmamalı.
	class Meta:
		model = SosyalMedia



admin.site.register(SosyalMedia,SosyalAdmin)

admin.site.register(Comment)

admin.site.register(Club)
admin.site.register(Fikstur)
admin.site.register(Hafta)

admin.site.register(Karakterler)
admin.site.register(TV)
admin.site.register(Yazi)
admin.site.register(Yazarlar)
