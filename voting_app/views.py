from .models import Event,Nominee
from django.shortcuts import render
from django.shortcuts import render, redirect
# Create your views here.


def homepage(request):
    events = Event.objects.all()
    context = {
        'events' : events
    }
    return render(request, 'homepage.html', context)


def nomination(request):
    if request.method == 'POST':
        form_data = request.POST
        form_files = request.FILES

        # Create a new instance of the Nominee model
        nominee = Nominee(
            nominee_name=form_data['nominee_name'],
            nominee_number=form_data['nominee_number'],
            nominee_email=form_data['nominee_email'],
            nominee_location=form_data['nominee_location'],
            # event=form_data['event'],
            category=form_data['category'],
            social_media=form_data['social_media'],
            nominee_picture=form_files['nominee_picture'],
            reason_for_filing=form_data['reason_for_filing']
        )
        # # Save the nominee object to the database
        nominee.save()
        # Redirect the user to the payment page
        # Replace 'payment_page' with the actual URL name or path of the payment page
        return redirect('homepage')
    # Update template name to 'nomination.html'
    return render(request, 'nomination.html')


def contestants(request, slug):
   event = Event.objects.get(slug=slug)
   context = {
       'event' : event
   }
   return  render( request, 'contestant.html', context)
