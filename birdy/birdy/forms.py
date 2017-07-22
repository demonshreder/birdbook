from django import forms


class BirdForm(forms.Form):
    bird_image = forms.ImageField()
