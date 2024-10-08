from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm

# Create your views here.
def home(request):
    all_members = Member.objects.all()
    return render(request, 'home.html', {"mem": all_members})

def join(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('join')  # Change this to the correct URL pattern name
    else:
        form = MemberForm()  # Initialize an empty form

    return render(request, 'login.html', {'form': form})
