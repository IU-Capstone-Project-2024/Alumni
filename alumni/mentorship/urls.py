from django.urls import path
# from .templates.mentorship import views
from . import views

urlpatterns = [
    path("", views.intro, name="intro"),
    path("form/", views.form, name="form"),
    path("thank_you/", views.thank_you, name="thank_you"),
]

