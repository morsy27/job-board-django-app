from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from job.models import Job
from .form import SignupForm
from django.contrib import messages
# Create your views here.

def main(request) :
    
    job_order_list = Job.objects.order_by('-published_at').all()
    job_leatest = job_order_list[:4]
    
    job_length = len(job_order_list)
    context = {'jobs': job_leatest , 'job_count':job_length}
    
    return render(request,'accounts/index.html', context)

def signup(request) :
    form = UserCreationForm()
    
    if request.method == 'GET':
        form = SignupForm()
        context = {'form': form}
        return render(request,'accounts/signup.html', context)
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid(): 
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request ,'Account Was Created For ' + user)
            return redirect('accounts:main')
            
    else :
        messages.error(request, 'Error Processing Your Request')
        context = {'form': form}
        return render(request,'accounts/signup.html', context)
        
    
    context = {'form': form}
    return render(request,'accounts/signup.html', context)

