from django import forms
from models import Event, Category
class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		exclude = ['author', 'pub_date']


class CategoryForm(forms.Form):
    category = forms.ChoiceField( required=True )
    #categories = forms.ModelChoiceField(queryset=Category.objects.all().order_by('title'))


