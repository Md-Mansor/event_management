from event.models import Category,Event,Participant
from django import forms


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields= "__all__"
        
class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields='__all__'
        widgets={
            'date': forms.SelectDateWidget(),
            'time': forms.TimeInput(attrs={'type':'time'}),
        } 
        
class ParticipantForm(forms.ModelForm):
    class Meta:
        model=Participant
        fields='__all__'