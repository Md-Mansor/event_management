from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")
def create(request):
    return render(request, "dashboard/create.html")
def event(request):
    return render(request, "dashboard/event.html")
def category_form(request):
    return render(request, "dashboard/category_form.html")