from django.shortcuts import render
from .models import Member
# Create your views here.
def home(request):
    all_members = Member.objects.all()
    return render(request,'home.html',{"mem":all_members})

def log(request):
    return render(request,'login.html',{})