from django import forms
from busroute.models import route

class routeForm(forms.ModelForm):
    class Meta:
        model = route
        fields = "__all__"

