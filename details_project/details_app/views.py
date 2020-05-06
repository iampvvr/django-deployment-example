from django.shortcuts import render
from django.http import HttpResponse
from details_app.models import Details
from . import forms
# Create your views here.

def details(request):
    r = Details.objects.all()
    reg_dict={'reg':r,'enter':'please enter'}
    return render(request,'details2.html',context=reg_dict)
def check(request):
    r = Details.objects.all()
    reg_dict={'reg':r,'enter':'Please enter'}
    return render(request,'details3.html',context=reg_dict)
def form_name_view(request):
    trail_dict={'enter':'please enter'}
    form = forms.regform()
    if request.method == 'POST':
        form = forms.regform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return details(request)
    return render(request,'details1.html',{'form':form})

# Create your views here.

# Create your views here.
