from django import forms
from .models import NADCPhotoComment, NADCPhoto


class PhotoCommentForm(forms.ModelForm):
    photo = forms.ModelChoiceField(
        queryset=NADCPhoto.objects.all(), widget=forms.HiddenInput()
    )

    class Meta:
        model = NADCPhotoComment
        fields = ("photo", "name", "comment")