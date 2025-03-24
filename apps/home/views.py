from django.shortcuts import render, redirect
from django.http import HttpResponse # Allows for raw HTTP output commands within the views.py for testing
import datetime; # Allows for the use of the datetime module to get the current date and time
from .models import Service
from .forms import ContactForm
from .models import Review
from .models import Promotion
from .models import TransformationVideo

CAPTCHAENABLED = True; # Set to True to enable captcha site-wide, False to disable

# Create a new view for the home page
def homeView(request):
    reviews = Review.objects.all().order_by('?')[:3]  # Fetch 3 random reviews
    return render(request, 'home.html', {'reviews': reviews})


# Create a new view for the about page, no arguments needed for it
def aboutView(request):
    return render(request,"about.html")

#Create a new view for the about us page, no arguments needed for it
def aboutUsView(request):
    return render(request,"about_us.html")

#Create a new view for the contact us page, no arguments needed for it 
def ContactUsView(request):
    if CAPTCHAENABLED:
        if request.method == 'POST':
            captchaForm = ContactForm(request.POST)
            if captchaForm.is_valid():
                # Process the form data
                pass
        else:
            captchaForm = ContactForm()
    else:
        captchaForm = None
    return render(request, "contact_us.html", {'form': captchaForm, 'captchaenabled': CAPTCHAENABLED})

# Create a new view for the gallery page
def galleryView(request):
    before_image_path = 'imgs/galleryLeftBefore.jpg'
    after_image_path = 'imgs/galleryLeftAfter.jpg'
    before_image_path_2 = 'imgs/galleryMiddleBefore.jpg'
    after_image_path_2 = 'imgs/galleryMiddleAfter.jpg'
    before_image_path_3 = 'imgs/galleryRightBefore.jpg'
    after_image_path_3 = 'imgs/galleryRightAfter.jpg'
    
    # Get all transformation videos, ordered by the 'order' field
    transformation_videos = TransformationVideo.objects.all().order_by('order')

    context = {
        'before_image1': before_image_path,
        'after_image1': after_image_path,

        'before_image2': before_image_path_2,
        'after_image2': after_image_path_2,
        
        'before_image3': before_image_path_3,
        'after_image3': after_image_path_3,
        
        'transformation_videos': transformation_videos
    }
    print("Context: ", context)

    return render(request, 'gallery.html', context)

# Create a new view for the schedule appintments page
# Return a list of services to be displayed on the schedule appointment page
def scheduleView(request):
    services = Service.objects.all()
    current_date = datetime.date.today()
    
    active_promotion = Promotion.objects.filter(
        start_date__lte=current_date,
        end_date__gte=current_date
    ).first()

    if CAPTCHAENABLED:
        if request.method == 'POST':
            captchaForm = ContactForm(request.POST)
            if captchaForm.is_valid():
                # Process the form data
                pass
        else:
            captchaForm = ContactForm()
    else:
        captchaForm = None

    return render(request, 'schedule_appointment.html', {
        'form': captchaForm,
        'captchaenabled': CAPTCHAENABLED,
        'services': services,
        'promotion': active_promotion
    })

# help code customer contact/continue
def submit_form(request):
    if request.method == 'POST':
        # Process form data here
        # just returns a simple response, a different team member can add functionality here
        return HttpResponse("Form submitted successfully.")
    else:
        return redirect('schedule_appointment')