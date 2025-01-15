from django import forms

class SignInForm(forms.Form):
    username = forms.CharField(max_length=100, label='Nazwa użytkownika')
    password = forms.CharField(max_length=100, label='Hasło', widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100, label='Nazwa użytkownika')
    password1 = forms.CharField(max_length=100, label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label='Powtórz Hasło', widget=forms.PasswordInput)
    address = forms.CharField(max_length=255, label='Adres')
    first_name = forms.CharField(max_length=255, label='Imię')
    last_name = forms.CharField(max_length=255, label='Nazwisko')
    phone = forms.CharField(max_length=16, label='Numer Telefonu')
    
class ContactForm(forms.Form):
    message = forms.CharField(max_length=512, widget=forms.Textarea, label='Wiadomość')

class OrderForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput, label='Data (dd/mm/yyyy)')
    days = forms.IntegerField(label='Liczba dni')
