from django import forms
from .models import NADCPhotoComment, NADCPhoto, WGNASPhotoComment, WGNASPhoto, NAPCPhotoComment, NAPCPhoto


class PhotoCommentForm(forms.ModelForm):
    photo = forms.ModelChoiceField(
        queryset=NADCPhoto.objects.all(), widget=forms.HiddenInput()
    )

    class Meta:
        model = NADCPhotoComment
        fields = ("photo", "name", "email", "comment")


class WGNASPhotoCommentForm(forms.ModelForm):
    photo = forms.ModelChoiceField(
        queryset=WGNASPhoto.objects.all(), widget=forms.HiddenInput()
    )

    class Meta:
        model = WGNASPhotoComment
        fields = ("photo", "name", "email", "comment")


class NAPCPhotoCommentForm(forms.ModelForm):
    photo = forms.ModelChoiceField(
        queryset=NAPCPhoto.objects.all(), widget=forms.HiddenInput()
    )

    class Meta:
        model = NAPCPhotoComment
        fields = ("photo", "name", "email", "comment")


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=11, label="Phone Number")
    message = forms.CharField(widget=forms.TextInput)


class DonateForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=11, label="Phone Number")
    amount = forms.IntegerField()
