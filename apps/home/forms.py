# apps/home/forms.py

from django import forms
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
    captcha = CaptchaField()