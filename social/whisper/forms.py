
from django import forms
from .models import *

class WhisperForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Whisper something...",
                "class": "textarea is-success is-medium",
                "style":"border-color:black"
            }
        ),
        label="",
    )

    class Meta:
        model = Whisper
        exclude = ("user", )