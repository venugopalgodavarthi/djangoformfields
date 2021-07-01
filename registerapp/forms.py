from django import forms

class RegisterF(forms.Form):
    #characters inputs
    name=forms.CharField(min_length=3,max_length=10)
    address=forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    firstname=forms.CharField(widget=forms.TextInput)
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    #hiddenpassword=forms.CharField(widget=forms.HiddenInput)
    
    #date inputs
    birthdate=forms.DateField()
    birth=forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    bi=['2019','2020','2021','2022']
    dateofbirth=forms.DateField(widget=forms.SelectDateWidget(years=bi))
    
    #number input
    intvalue=forms.IntegerField()
    floatvalue=forms.FloatField()
    decvalue=forms.DecimalField()
    
    #boolean input
    agree=forms.BooleanField()
    
    #choice inputs
    list1=[('Male','MALE'),('Female','FEMALE')]
    gender=forms.ChoiceField(choices=list1)
    
    list2=[('Male','MALE'),('Female','FEMALE')]
    person=forms.ChoiceField(widget=forms.RadioSelect, choices=list2)
    
    fav_color=[('Red','RED'),('Green','GREEN'),('Pink','PINK'),('White','WHITE')]
    color=forms.MultipleChoiceField(choices=fav_color)
    
    fav=[('Red','RED'),('Green','GREEN'),('Pink','PINK'),('White','WHITE')]
    colorfav=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=fav)
    
    #files input
    images=forms.ImageField()
    files=forms.FileField()
    #file=forms.FilePathField()
    
    