from blog.models import*
from django.shortcuts import *

def blog(request):

    latest_blogs = Blog.objects.order_by("-created_at")[:6]
    context = {"latest_blogs": latest_blogs}
    context['tags']=Tag.objects.all()

    if request.user.is_authenticated:
        notifications = Notification.objects.filter(all_user=request.user)
        privetnotif=Notification.objects.filter(user=request.user)
        total=notifications.count()+privetnotif.count()
        context.update({'notifications': notifications,'privetnotif':privetnotif,'total':total})

    return context
