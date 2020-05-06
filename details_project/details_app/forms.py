from django import forms
from django.core import validators
from details_app.models import Details

class regform(forms.ModelForm):
    class Meta:
        model = Details
        fields = "__all__"
