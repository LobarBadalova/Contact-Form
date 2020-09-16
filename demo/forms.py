from django.forms import ModelForm
from django import forms
from .models import Contact

class DateTimeInput(forms.DateInput):
	input_type='datetime-local'


class ContactForm(ModelForm):
	class Meta:
		model=Contact
		fields=('__all__')
		widgets = {
		'fname':forms.TextInput(attrs={'class': 'input--style-1','placeholder':"NAME"}),
		'lname':forms.TextInput(attrs={'class': 'input--style-1','placeholder':"LASTNAME"}),
		'email':forms.EmailInput(attrs={'class': 'input--style-1','placeholder':"EMAIL ADRESS"}),
		'date': DateTimeInput(attrs={'class': 'input--style-1','placeholder':"DATE OF APPOINTMENT"})}



    # fname = forms.CharField(label='Your name', max_length=100)
    # lname = forms.CharField(label='Your  lastname', max_length=100)
    # phone = forms.IntegerField(label='Your  phone number')
    # time=forms.DateTimeField(help_text='Enter date and time of appointment')
    
