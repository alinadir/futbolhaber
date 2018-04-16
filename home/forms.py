from django import forms
from .models import Yorum
from captcha.fields import ReCaptchaField

class CommentForm(forms.ModelForm):
	captcha = ReCaptchaField()
	class Meta:
		model = Yorum
		fields = [
			'isim',
			'yorumunuz',
		]