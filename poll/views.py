from django.shortcuts import render

from .models import Question


def index(request):
	context = {}
	questions_query= Questions.objects.all()
	context ['question'] = questions_query
	return render(request, 'poll/index.html',context)

def help_me(request):
	context = {}
	return render(request, 'poll/helpme.html',context)

def detail_question(request, question_id):
	context = {}
	question_query= Question.objects.get(id=question_id)
	context['question'] = question_query
	return render(request, 'poll/detail_question.html', context)

