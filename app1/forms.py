from django import forms
from app1.models import Topico, DadosForm


class FormName(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    texto = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("GOTCHA BOT!")
        return botcatcher

class ModelForm1(forms.ModelForm):
    class Meta:
        model = DadosForm
        fields = "__all__"