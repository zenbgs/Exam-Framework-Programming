from django.forms import ModelForm
from landingpage.models import Tanaman
 
class TanamanForm(ModelForm):
    class Meta:
        model=Tanaman
        fields="__all__"