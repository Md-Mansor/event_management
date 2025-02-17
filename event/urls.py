from django.urls import path
from event.views import home,event
urlpatterns = [
    path("", home),
    path("dashboard/", event),
]
