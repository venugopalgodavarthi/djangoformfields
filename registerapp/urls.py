from django.urls import path
from registerapp import views
my_app='registerapp'

urlpatterns = [
    path('sample/',views.registerp,name="sample"),

]