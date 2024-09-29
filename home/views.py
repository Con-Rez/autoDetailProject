from django.shortcuts import render
from django.http import HttpResponse # Allows for raw HTTP output commands within the views.py for testing
import datetime; # Allows for the use of the datetime module to get the current date and time

# Create your views here.
def homeView(request):
    # This can override the HTML file in its entirety!
    # return HttpResponse("Hello world, this is a python file output!") 

    # Create and pass variable to home.html to say the current time
    today = datetime.datetime.now().date() 
    return render(request,"home.html", {"today": today})