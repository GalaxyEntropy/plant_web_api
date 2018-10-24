from django.template import loader
# Create your views here.
from .models import Question,Choice
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404,render
from django.views import generic

#def index(request):
#	lastest_question_list = Question.objects.order_by('-pub_date')[:5]
#	template = loader.get_template('polls/index.html')
#	context = {
#		'lastest_question_list':lastest_question_list,
#	}
#	return HttpResponse(template.render(context,request))
'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
def detail(request,question_id):
	#try:
	question = get_object_or_404(Question,pk=question_id)
		#question = Question.objects.get(pk=question_id)
	#except Question.DoesNotExist:
	#	raise Http404("Question does not exist")
	return render(request,'polls/detail.html',{'question':question})	
#	return HttpResponse("You are looking at question %s"% question_id);

def vote(request,question_id):
	question = get_object_or_404(Question,pk=question_id)
	try:
		selected_choice=question.choice_set.get(pk=request.POST['choice'])
	except(KeyError,Choice.DoesNotExist):
		return render(request,'polls/detail.html',{
		'question':question	,
		'error_message':"You didn't select a choice."	
		})
	else:
		selected_choice.votes+=1
		selected_choice.save()	
		return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
	#return HttpResponse("You are voting on question %s" % question_id)
'''
'''
def index(request):
	latest_question_list=Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list':latest_question_list,
	}
	#output=', '.join([q.question_text for q in lastest_question_list])
	return HttpResponse(template.render(context,request))
'''
'''
def results(requests,question_id):
	response = "You are lokking at the result of question %s."
	return HttpResponse(response % question_id)
'''
'''
def results(request,question_id):
	question=get_object_or_404(Question,pk=question_id)
	return render(request,'polls/results.html',{'question':question})
'''


class IndexView(generic.ListView):
	template_name='polls/index.html'
	context_object_name = 'latest_question_list'
	
	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model=Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name='polls/results.html'

def vote(request,question_id):
	question = get_object_or_404(Question,pk=question_id)
	try:
		selected_choice=question.choice_set.get(pk=request.POST['choice'])
	except(KeyError,Choice.DoesNotExist):
		return render(request,'polls/detail.html',{
		'question':question	,
		'error_message':"You didn't select a choice."	
		})
	else:
		selected_choice.votes+=1
		selected_choice.save()	
		return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
	

def get_queryset(self):
	return Question.onjects.filter(
		pub_date__lte=timezone.now()

	).order_by('-pub_date')[:5]



