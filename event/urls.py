from django.urls import path
from event.views import home,create,event,category_form,event_form,participant_form,participant,all_events
urlpatterns = [
    path("", home, name="home"),
    path("create/", create, name="create") ,
    path("event/",event , name="view"),
    path("category_form/",category_form , name="category_form"),
    path("event_form/",event_form , name="event_form"),
    path("participant_form/",participant_form , name="participant_form"),
    path("participant/",participant , name="participant"),
    path("all_events/",all_events , name="all_events"),
]
