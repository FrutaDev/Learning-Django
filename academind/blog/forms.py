from django import forms
from .models import Subscriber

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = "__all__"
        labels = {
            'email': 'Suscríbete'
        }
        error_messages = {
            'email': {
                'required': 'Por favor inserta un email válido.',
            }
        }
        widget = {
            "email": forms.EmailInput(attrs={
                "placeholder": "Ingresa tu correo electrónico"
            })
        }   