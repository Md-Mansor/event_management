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
    return render(request, "dashboard/category_form.html")


def create_category(request):
    # category_form=Category.objects.all()
    form=CategoryForm()

    if request.method=="POST":
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "dashboard/category_form.html",{"form":form,"message":"Category created successfully"})
    context={"form":form}
    return render(request, "dashboard/category_form.html",context)