from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    message = forms.CharField(label='Message', widget=forms.Textarea)
