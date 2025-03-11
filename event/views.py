from django.shortcuts import render
from event.forms import CategoryForm,EventForm,ParticipantForm
from event.models import Category,Event,Participant
from datetime import datetime
from django.db.models import Count ,Q,Max,Min, Avg
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    events = Event.objects.all()
    context = {
        "events": events
    }
    # print(events)
    return render(request, "home.html", context)

def create(request):
    return render(request, "dashboard/create.html")

def event(request):
    query = request.GET.get("q")
    events = Event.objects.select_related("category").prefetch_related("event").all()

    # count events & participant
    counts = Event.objects.aggregate(
        total_participant=Count("participant"),
        total_events=Count("id"),
        # upcoming=Count("date",filter(Q(date__gt=datetime.now().date()))),
        # past=Count("date",filter(Q(date__lt=datetime.now().date()))),
        )


    # query result conditionals
    today_event=Event.objects.filter(date=datetime.now().date())
    if query == "all":
        today_event = Event.objects.all()
    elif query == "upcoming":
        today_event=Event.objects.filter(date__gt=datetime.now().date())
    elif query == "past":
        today_event=Event.objects.filter(date__lt=datetime.now().date())
    
    context = {
        "today_event":today_event,
        "counts":counts,
    }
    return render(request, "dashboard/dashboard_main.html",context)


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


def delete(request, id):
    if request.method == "POST":
        event=Event.objects.get(id=id)
        event.delete()
        return redirect("view")


def edit(request, id):
    event = Event.objects.get(id=id)
    event_form = EventForm(instance=event)

    if request.method=="POST":
        event_form=EventForm(request.POST,instance=event)
        if event_form.is_valid():
            event_form.save()
            
            return redirect("view")
    context={"event_form": event_form}
    return render(request, "dashboard/event_form.html", context)
