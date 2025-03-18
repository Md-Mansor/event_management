from event.models import Category, Event, Participant
from django import forms

class StyledFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_style()

    default_class = (
        "border border-gray-300 rounded-md p-3 m-2 w-full shadow-sm "
        "focus:border-blue-500 focus:ring focus:ring-blue-200 transition-all duration-200"
    )

    def apply_style(self):
        for field_name, field in self.fields.items():
            common_attrs = {
                "class": self.default_class,
                "placeholder": f"Enter {field.label.lower()}",
            }
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update(common_attrs)
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    **common_attrs,
                    "rows": 4,
                    "class": f"{self.default_class} resize-none",
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    "class": f"{self.default_class} cursor-pointer",
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    "class": "space-y-2 p-2",
                })
            elif isinstance(field.widget, forms.EmailInput):
                field.widget.attrs.update(common_attrs)

class CategoryForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(),
            "description": forms.Textarea(),
        }

class EventForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        widgets = {
            "date": forms.SelectDateWidget(),
            "time": forms.TimeInput(attrs={"type": "time"}),
            "category": forms.Select(),
        }

class ParticipantForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Participant
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(),
            "event": forms.CheckboxSelectMultiple(),
        }