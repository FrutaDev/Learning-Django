from django import forms
from .models import Subscriber, Comment

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
        widgets = {
            "email": forms.EmailInput(attrs={
                "placeholder": "Ingresa tu correo electrónico"
            })
        }   


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["user_name", "text"]
        labels = {
            "text": "Tu comentario"
        }
        error_messages = {
            "text": {
                "required": "Por favor inserta un comentario."
            }
        }
        widgets = {
            "user_name": forms.TextInput(attrs={
                "placeholder": "Tu nombre"
            }),
            "text": forms.Textarea(attrs={
                "placeholder": "Tu comentario"
            })
        }