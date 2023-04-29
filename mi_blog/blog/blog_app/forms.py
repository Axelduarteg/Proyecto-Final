from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterUserCreationForm(UserCreationForm):
   email = forms.EmailField(label="Email Usuario")
   password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput, help_text=None)
   password2=forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, help_text=None)

   class Meta:
      model=User
      fields=["username","email","password1","password2"]
      help_texts={k:"" for k in fields}

class UserEditForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']
        help_texts={k:"" for k in fields}
        widgets = {
            'username': forms.TextInput(attrs={'autocomplete': 'off'}),
            'email': forms.EmailInput(attrs={'autocomplete': 'off'}),
        }

class PasswordChangeForm(forms.ModelForm):
    new_password1 = forms.CharField(
        label='New password',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )
    new_password2 = forms.CharField(
        label='New password confirmation',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )

    class Meta:
        model = User
        fields = []

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['new_password1'])
        if commit:
            user.save()
        return user
        

