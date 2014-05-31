from django import forms

class LoyaltyForm(forms.Form):
	name = forms.CharField(max_length=100, label='Your Name')
	email = forms.EmailField(required = False, label='Your Email')
	yearsSubscribed = forms.CharField(widget=forms.Textarea, required=False, label='How many years have you been an ASO season ticket subscriber?')
	improve = forms.CharField(widget=forms.Textarea, required=False, label='In a few words, what can we do to improve your symphony experience?')
	favorite = forms.CharField(widget=forms.Textarea, required=False, label='What was your all-time favorite Pops concert?  Masterworks?')
