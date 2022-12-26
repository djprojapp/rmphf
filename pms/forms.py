from django import forms
from . models import Adjustment

class AdjustmentForm(forms.ModelForm):
    class Meta:
        model=Adjustment
        fields=["ppo","description","amount","p_type"]