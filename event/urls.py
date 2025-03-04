from django.urls import path
from event.views import home,create,event,category_form
urlpatterns = [
    path("", home, name="home"),
    path("create/", create, name="create") ,
    path("event/",event , name="view"),
    path("category_form/",category_form , name="category_form"),
]
