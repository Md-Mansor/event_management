from django.forms import ModelForm
from event.models import Category,Event,Participant
class CategoryForm(ModelForm):
    class Meta:
        model=Category
        fields='__all__'
        
class EventForm(ModelForm):
    class Meta:
        model=Event
        fields='__all__'
        
class ParticipantForm(ModelForm):
    class Meta:
        model=Participant
        fields='__all__'