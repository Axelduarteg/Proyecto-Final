from django import forms

class SendMessageForm(forms.Form):
    message = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Escribe tu mensaje aquí'}))
    receiver_id = forms.IntegerField(widget=forms.HiddenInput())
