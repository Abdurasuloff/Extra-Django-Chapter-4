from django.shortcuts import render, redirect
from .forms import MyUserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from .tasks import send_mail_task, slow_func
from .models import Notification
from django.utils.timezone import datetime
from django.http import HttpResponse
from .utils import send_notification
# Create your views here.

subject = 'E-Marketga xush kelibsiz'
message = "Assalomu alaykum, {}. Bizning saytimizdan foydalanyotganizgiz uchun rahmat."


def index(request):
    # notifications = Notification.objects.filter(datetime__date=datetime.now().date(), sent=True)
    return render(request, "index.html", )



def signup(request):
    form = MyUserCreationForm()
    if request.method == "POST":
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            user =  form.save()
            send_mail_task.delay(subject, message.format(user.username), [user.email])
            return redirect('index')
            
        else:
            return render(request, "signup.html", {'form':form})    
        
    return render(request, "signup.html", {'form':form})



def test_send(request):
    send_notification("Viewdan kelgan bildirishnoma")
    return HttpResponse("Ok")