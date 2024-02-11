# views.py
from django.shortcuts import render, redirect
from .form import feebBackForm # Updated import for better naming conventions
from django.contrib import messages  # Import messages module for feedback messages

def feedback(request):
    if request.method == 'POST':
        form = feebBackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your feedback!')  # Provide feedback to the user
            return redirect('/')  # Redirect to the home page or appropriate URL
        else:
            messages.error(request, 'There was an error in the form. Please check and try again.')  # Provide error feedback
    else:
        form = feebBackForm()

    context = {'form': form}
    # return redirect('/')
    return render(request, 'feedback.html', context)
    # return NULL
