from django import forms

class DiscussionForm(forms.Form):
    topic = forms.CharField(label='topic', max_length=1000)
    text = forms.CharField(label='text', max_length=5000)