
from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect
# Download the helper library from https://www.twilio.com/docs/python/install


def index(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('')
	else:
		form = ContactForm()
	return render(request, 'index.html', {'form': form})
