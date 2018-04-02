from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView
from .forms import CommentForm
from .models import search_by_tag


# не хорошо, нужено переделать в отдельный файл
OK = 0
INCORRECT_INPUT = 1
ONLY_POST_REQ = 2


QUESTIONS = {
   	'1' : {"id":1, "question_title":"To be or not to be", "question_text":"That's the question", "author":"Nik",
   		"date_creation":101, "tags":["shaksper", "william"], "rating":100500, "comments_count":3},
   	'2' : {"id":2, "question_title":"To be or not to be", "question_text":"That's the question", "author":"Nik",
   		"date_creation":101, "tags":["shaksper", "william"], "rating":100, "comments_count":3},
   	'2' : dict(id=2, question_title="To be or not to be", question_text="That's the question", author="Nik",
   		date_creation=101, tags=["shaksper", "william"], rating=100, comments_count=4),
	'3' : dict(id=3, question_title="lool", question_text="here", author="Nik",
   		date_creation=101, tags=["c++", "python"], rating=100, comments_count=6),
   	'4' : dict(id=4, question_title="To be or not to be", question_text="That's the question", author="Nik",
   		date_creation=101, tags=["shaksper", "william"], rating=100, comments_count=1),
   	'5' : dict(id=5, question_title="To be or not to be", question_text="That's the question", author="Nik",
   		date_creation=101, tags=["shaksper", "william"], rating=100, comments_count=1),
   	'6' : dict(id=6, question_title="To be or not to be", question_text="That's the question", author="Nik",
   		date_creation=101, tags=["shaksper", "william"], rating=100, comments_count=1),
   	'7' : dict(id=7, question_title="To be or not to be", question_text="That's the question", author="Nik",
   		date_creation=101, tags=["shaksper", "william"], rating=100, comments_count=1)
   	}


def paginate(objects_list, request):
	paginator = Paginator(objects_list, 2)
	# template = loader.get_template('questions/index.html')
	page = request.GET.get('page')
	try:
		objects_page = paginator.page(page)
	except PageNotAnInteger:
		objects_page = paginator.page(1)
	except EmptyPage:
		objects_page = paginator.page(paginator.num_pages)
	# do smth with Paginator, etc…
	return objects_page, paginator


# Create your views here.
def index(request):
	questions = list(QUESTIONS.values())
	template = loader.get_template('questions/index.html')
	current_page, paginator = paginate(questions, request)
	context = {
	'questions': current_page,
	}
	return HttpResponse(template.render(context, request))


def tag(request, tag=None):
    print("TAG : ", tag)
    try:
    	questions = search_by_tag(list(QUESTIONS.values()), tag)
    except Exception as e:
    	questions = list(QUESTIONS.values())
    template = loader.get_template('questions/tag.html')
    current_page, paginator = paginate(questions, request)
    context = {
    'questions': current_page,
    }
    return HttpResponse(template.render(context, request))


QUESTIONS_HOT = {
   	'1' : {"id":1, "question_title":"To be or not to be", "question_text":"That's the question", "author":"Nik",
   		"date_creation":101, "tags":["shaksper", "william"], "rating":100500, "comments_count":3},
   	'2' : {"id":2, "question_title":"To be or not to be", "question_text":"That's the question", "author":"Nik",
   		"date_creation":101, "tags":["shaksper", "william"], "rating":100, "comments_count":3},
   	'2' : dict(id=2, question_title="To be or not to be", question_text="That's the question", author="Nik",
   		date_creation=101, tags=["shaksper", "william"], rating=100, comments_count=4),
	'3' : dict(id=3, question_title="lool", question_text="here", author="Nik",
   		date_creation=101, tags=["c++", "python"], rating=100, comments_count=6),
   	}


def hot(request):
    questions = list(QUESTIONS_HOT.values())
    template = loader.get_template('questions/tag.html')
    current_page, paginator = paginate(questions, request)
    context = {
    'questions': current_page,
    }
    return HttpResponse(template.render(context, request))


COMMENTS = [
	dict(id=1, comment_text="Be", correct_answer=False, comment_author="Nik"),
	dict(id=2, comment_text="Not Be", correct_answer=True, comment_author="Nik"),
	dict(id=3, comment_text="Be", correct_answer=False, comment_author="Nik"),
	dict(id=4, comment_text="Be", correct_answer=True, comment_author="Nik"),
	dict(id=5, comment_text="Это будет ооооооооочень просто ультра какой нереально длинный комментарий, ах, да, это ответ, а не комментарий, ну не суть. Так вот, быть или не быть вот в чем вопрос? ооооооооочень филосовская тема, на самом деле, вот 100500 вводных слов, точно быть в этом ответе.", useful=True, comment_author="Nik"),
	dict(id=3, comment_text="Be", correct_answer=False, comment_author="Nik"),
	]


def get_comment(request):
	# if this is a POST request we need to process the form data
	comment = ""
	max_lenght = 1000
	template = loader.get_template('questions/question.html')
	if request.method == 'POST':
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			comment = comment_form.cleaned_data["comment"]
			context = {
			'error' : 0,
			'error_message' : '',
			'max_lenght' : max_lenght
			}
			return context
			#HttpResponse(template.render(context, request))
		else:
			context = {
			'error' : INCORRECT_INPUT,
			'error_message' : 'Количество символов превышет ' + str(max_lenght),
			'max_lenght' : max_lenght
			}
			return context
			#HttpResponse(template.render(context, request))
	else:
		context = {
		'error' : ONLY_POST_REQ,
		'error_message' : 'Допустима обработка только GET запроса',
		'max_lenght' : max_lenght
		}
		return context
		#HttpResponse(template.render(context, request))


def detail(request):
	
	


	question_data = dict(id=1, question_title="To be or not to be", question_text="That's the question", author="Nik",
   		date_creation=101, tags=["shaksper", "william"], rating=100)

	comments_data = COMMENTS
	current_page, paginator = paginate(comments_data, request)
	
	add_context = get_comment(request)
	template = loader.get_template('questions/question.html')
	
	context = {
        'question' : question_data,
        'comments' : current_page,
        'error_in_comment' : add_context["error"],
        'error_in_comment_message' : add_context["error_message"],
        'comment_max_lenght' : add_context["max_lenght"],
        'OK' : OK,
        'INCORRECT_INPUT' : INCORRECT_INPUT,
        'ONLY_POST_REQ' : ONLY_POST_REQ,

    }
	return HttpResponse(template.render(context, request))


def ask(request):
	
	add_context = get_comment(request)
	template = loader.get_template('questions/ask.html')
	
	if request.method == 'POST':
		form = AskForm(request.POST)

		if form.is_valid():
			# comment = signup_form.cleaned_data["comment"]
			new_question = form.cleaned_data["username"]
			info = form.cleaned_data["info"]
			tags = form.cleaned_data["tags"]
			# avatar = signup_form.cleaned_data["avatar"]

			context = {
			'error_in_signup' : error_in_signup,
			'error_in_signup_message' : error_in_signup_message,

			'INCORRECT_INPUT' : INCORRECT_INPUT,
			}
			return HttpResponse(template.render(context, request))
		else:
			context = {
			'error_in_signup' : INCORRECT_INPUT,
			'error_in_signup_message' : 'Неправильно введены данные',

			'INCORRECT_INPUT' : INCORRECT_INPUT,

			}
			print("-")
			return HttpResponse(template.render(context, request))
	else:
		context = {
		'error_in_signup' : ONLY_POST_REQ,
		'error_in_signup_message' : 'Допустима обработка только GET запроса',

		'INCORRECT_INPUT' : INCORRECT_INPUT,
		}
		return HttpResponse(template.render(context, request))



def popular_tags(request):
    return dict(popular_tags=['c++', 'python', 'go', 'perl', 'c#', "shaksper", "william" ])


def best_members(request):
    return dict(best_members=['me', 'again me', 'always me', 'lool'])
