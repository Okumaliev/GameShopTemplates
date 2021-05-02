from django import forms
from .models import Order


class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def clean_data(self):
        data = self.cleaned_data
        phone = data.get('phone')
        if not phone.startswith('+996'):
            raise forms.ValidationError('Только кыргызские номера')
        return phone