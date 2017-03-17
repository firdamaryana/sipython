from django.shortcuts import render


def index(request):
	context = ()
	return render(request, 'poll/index.html',context)

def help_me(request):
	context = ()
	return render(request, 'poll/helpme.html',context)
