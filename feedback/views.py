# views.py
from django.shortcuts import render,redirect
from .form import feebBackForm
# Create your views here.

def feedback(request):
    form = feebBackForm()
    if request.method == 'POST':
        # print(request.POST)
        # extract all the data and write it to the database
        form = feebBackForm(request.POST)
        if form.is_valid():
            # print(request.POST)
            form.save()
        # means return to the main page
        return redirect('/')


    context = {'form':form}
    return render(request,'feedBack.html',context)

