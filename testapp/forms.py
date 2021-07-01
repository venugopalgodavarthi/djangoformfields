from django import forms


class loginform(forms.Form):
    username =forms.CharField(help_text="plz enter the username")
    password =forms.CharField(widget=forms.PasswordInput)
    age= forms.IntegerField(widget=forms.TextInput,min_value=18, max_value=30,error_messages="plz enter the value above 18 and below 30")
    address= forms.IntegerField(widget=forms.Textarea)
    img=forms.ImageField(required=False)