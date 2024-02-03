from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path("", views.HomeView.as_view(), name="main"),
    path("contact-us", views.ContactView.as_view(), name="contact"),
    path("about-us", views.AboutUsView.as_view(), name="about-us"),
]
