from django.forms import ModelForm
from .models import feedBacks

# this page is for creating forms

class feebBackForm(ModelForm):
    class Meta:
        model = feedBacks
        fields = '__all__'