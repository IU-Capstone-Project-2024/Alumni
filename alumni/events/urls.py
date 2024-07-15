from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", views.page, name="events"),
    path("filter_events/", views.filter_events, name="filter_events"),
    path("ai-recommendation/", views.ai_recommendation, name="ai_recommendation"),
    path("<str:event_link>/", views.event_detail, name='event_detail'),
]
