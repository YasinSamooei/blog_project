from django.shortcuts import redirect
from django.views.generic import CreateView,TemplateView,ListView
from django.contrib import messages

# local
from blog.models import Blog
from .models import Contact
from .forms import ContactForm
from accounts.models import User


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['comments'] = Contact.objects.all().order_by("-created_at")[:3]

        blogs=Blog.objects.order_by('-created_at')
        context['blogs'] = blogs[:6]
         
        return context


class ContactView(CreateView):
    template_name = 'home/contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Your comment was successfully registered.")
        return redirect("home:contact")


class AboutUsView(ListView):
    template_name='home/about-us.html'
    queryset = User.objects.filter(is_staff=True)