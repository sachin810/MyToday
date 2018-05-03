from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        q_s = User.objects.filter(email=email)
        if q_s.exists():
            raise forms.ValidationError("This Email Already Exists")
        return email

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


    def clean(self, *args,**kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('This user does not exist')
        if not user.check_password(password):
            raise forms.ValidationError('Incorrect Password')
        if not user.is_active:
            raise forms.ValidationError('This user is not active')

        return super(LoginForm, self).clean(*args,**kwargs)


class UpdateForm(forms.ModelForm):
    username = forms.CharField(label="Username")
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name'
        ]

    def clean_confirm_new_password(self):
        new_password = self.cleaned_data.get('new_password')
        confirm_new_password = self.cleaned_data.get('confirm_new_password')
        if new_password != confirm_new_password:
            raise forms.ValidationError('Password Does not match')
        return new_password
