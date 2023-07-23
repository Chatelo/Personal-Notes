from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels ={'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title','text']
        labels = {'title': 'Title', 'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        
class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)


        