from django.contrib import admin
from .models import Ülke,Oyuncu,Takım,Fikstur,Hafta,Sezon,Yardımcılar,Hoca,Yoneticiler,Stadyum,İdman,LigKupa,GolEkle1,AsistEkle1,SarıEkle1,KırmızıEkle1,GolEkle2,AsistEkle2,SarıEkle2,KırmızıEkle2,Hakemler

# Register your models here.

admin.site.register(Ülke)
admin.site.register(Oyuncu)
admin.site.register(Fikstur)
admin.site.register(Takım)
admin.site.register(Hafta)
admin.site.register(Sezon)
admin.site.register(Yardımcılar)
admin.site.register(Hoca)
admin.site.register(Yoneticiler)
admin.site.register(Stadyum)
admin.site.register(İdman)
admin.site.register(GolEkle1)
admin.site.register(AsistEkle1)
admin.site.register(SarıEkle1)
admin.site.register(KırmızıEkle1)
admin.site.register(LigKupa)
admin.site.register(GolEkle2)
admin.site.register(AsistEkle2)
admin.site.register(SarıEkle2)
admin.site.register(KırmızıEkle2)
admin.site.register(Hakemler)

