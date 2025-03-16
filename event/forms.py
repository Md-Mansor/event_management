from event.models import Category,Event,Participant
from django import forms

class styledFormMixin:

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.apply_style()

    default_class="border-2 border-gray-300 rounded-md p-2 m-2 w-full shadow-md"

    def apply_style(self):
        for field_name , field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    "class":self.default_class,
                    "placeholder":f"Enter {field.label.lower() }"
                    })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    "class":self.default_class,
                    "placeholder":f"Enter {field.label.lower() }"
                    })
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    "class":self.default_class,
                    })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    "class":"space-y-2",
                    })
            elif isinstance(field.widget, forms.EmailInput):
                field.widget.attrs.update({
                    "class":self.default_class,
                    "placeholder":f"Enter {field.label.lower() }"
                    })

class CategoryForm(styledFormMixin,forms.ModelForm):
    class Meta:
        model=Category
        fields= "__all__"
        widgets={
            'name':forms.TextInput(),
            'description':forms.Textarea()
        }
        
class EventForm(styledFormMixin,forms.ModelForm):
    class Meta:
        model=Event
        fields='__all__'
        widgets={
            'date': forms.SelectDateWidget(),
            'time': forms.TimeInput(attrs={'type':'time'}),
            'category':forms.Select(),            
        }   
    
class ParticipantForm(styledFormMixin,forms.ModelForm):
    class Meta:
        model=Participant
        fields='__all__'
        widgets={
            'name':forms.TextInput(),
            'event':forms.CheckboxSelectMultiple()
        }