from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User


class RegisterUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email Usuario")
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput,
        help_text="La contraseña debe contener al menos 8 caracteres y no debe incluir caracteres especiales.",
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput,
        help_text=None,
    )

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
        help_texts = {k: "" for k in fields}
        
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email',)

    def clean_email(self):
        email = self.cleaned_data['email']
        # Verificar si el email ya existe en otro usuario
        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está en uso.')
        return email


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Contraseña actual', widget=forms.PasswordInput)

    class Meta:
        model = User

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise forms.ValidationError('La contraseña actual es incorrecta.')
        return old_password
    
class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")
