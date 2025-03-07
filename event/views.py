from django.shortcuts import render
from event.forms import CategoryForm,EventForm,ParticipantForm
from event.models import Category,Event,Participant

# Create your views here.
def home(request):
    return render(request, "home.html")

def create(request):
    return render(request, "dashboard/create.html")

def event(request):
    return render(request, "dashboard/event.html")


def category_form(request):
    category_form = CategoryForm()

    if request.method=="POST":
        category_form=CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return render(request, "dashboard/category_form.html",{"form":category_form,"message":"Category created successfully"})
    context={"category_form": category_form}
    return render(request, "dashboard/category_form.html", context)

def event_form(request):
    event_form = EventForm()

    if request.method=="POST":
        event_form=EventForm(request.POST)
        if event_form.is_valid():
            event_form.save()
            return render(request, "dashboard/event_form.html",{"form":event_form,"message":"Event created successfully"})
    context={"event_form": event_form}
    return render(request, "dashboard/event_form.html", context)

def participant_form(request):
    participant_form = ParticipantForm()

    if request.method=="POST":
        participant_form=ParticipantForm(request.POST)
        if participant_form.is_valid():
            participant_form.save()
            return render(request, "dashboard/participant_form.html",{"form":participant_form,"message":"Participant created successfully"})
    context={"participant_form": participant_form}
    return render(request, "dashboard/participant_form.html", context)