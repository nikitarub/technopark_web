from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import SignupForm, LoginForm
# Create your views here.

# не хорошо, нужено переделать в отдельный файл
OK = 0
INCORRECT_INPUT = 1
ONLY_POST_REQ = 2


USERS = [
dict(
        current_user=dict(
        	id=1,
        	username="Nik",
        	logged=1,
            firstname='Nikita',
            lastname='Rubinov',
            email='lol@looool.ru'            
        ),
    )
]

def current_user(request):
	return USERS[0]


def user_settings(request):
	user = USERS[0]
	template = loader.get_template('users/user_settings.html')

	username = user["current_user"]["username"]
	firstname = user["current_user"]["firstname"]
	lastname = user["current_user"]["lastname"]
	email = user["current_user"]["email"]
	
	error_in_signup_message = ""
	error_in_signup = OK

	if request.method == 'POST':
		signup_form = SignupForm(request.POST)

		if signup_form.is_valid():
			# comment = signup_form.cleaned_data["comment"]
			username = signup_form.cleaned_data["username"]
			firstname = signup_form.cleaned_data["firstname"]
			lastname = signup_form.cleaned_data["lastname"]
			email = signup_form.cleaned_data["email"]
			
			# avatar = signup_form.cleaned_data["avatar"]

			context = {
			'username' : username,
			'firstname' : firstname,
			'lastname' : lastname,
			'email' : email,

			'error_in_signup' : error_in_signup,
			'error_in_signup_message' : error_in_signup_message,

			'INCORRECT_INPUT' : INCORRECT_INPUT,
			}
			return HttpResponse(template.render(context, request))
		else:
			context = {
			'username' : username,
			'firstname' : firstname,
			'lastname' : lastname,
			'email' : email,

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


def signup_user(request):
	user = current_user(request)
	max_lenght = 1000
	template = loader.get_template('users/signup.html')

	username = ""
	firstname = ""
	lastname = ""
	email = ""
	avatar = ""
	error_in_signup_message = ""
	error_in_signup = OK

	if request.method == 'POST':
		signup_form = SignupForm(request.POST)

		if signup_form.is_valid():
			# comment = signup_form.cleaned_data["comment"]
			username = signup_form.cleaned_data["username"]
			firstname = signup_form.cleaned_data["firstname"]
			lastname = signup_form.cleaned_data["lastname"]
			email = signup_form.cleaned_data["email"]
			password = signup_form.cleaned_data["password"]
			confirm_password = signup_form.cleaned_data["confirm_password"]
			# avatar = signup_form.cleaned_data["avatar"]

			if password != confirm_password:
				error_in_signup_message = "Неверный пароль"
				error_in_signup = INCORRECT_INPUT

			context = {
			"username" : username,
			"firstname" : firstname,
			"lastname" : lastname,
			"email" : email,
			"password" : "",
			"avatar" : avatar,
			'error_in_signup' : error_in_signup,
			'error_in_signup_message' : error_in_signup_message,
			'max_lenght' : max_lenght,

			'INCORRECT_INPUT' : INCORRECT_INPUT,
			}
			return HttpResponse(template.render(context, request))
		else:
			context = {
			"username" : username,
			"firstname" : firstname,
			"lastname" : lastname,
			"email" : email,
			"password" : "",
			"avatar" : avatar,
			'error_in_signup' : INCORRECT_INPUT,
			'error_in_signup_message' : 'Неправильно введены данные',
			'max_lenght' : max_lenght,

			'INCORRECT_INPUT' : INCORRECT_INPUT,

			}
			print("-")
			return HttpResponse(template.render(context, request))
	else:
		context = {
		"username" : "",
		"firstname" : "",
		"lastname" : "",
		"email" : "",
		"password" : "",
		"avatar" : "",
		'error_in_signup' : ONLY_POST_REQ,
		'error_in_signup_message' : 'Допустима обработка только GET запроса',
		'max_lenght' : max_lenght,

		'INCORRECT_INPUT' : INCORRECT_INPUT,
		}
		return HttpResponse(template.render(context, request))


def login_user(request):

	template = loader.get_template('users/login.html')

	username = ""
	firstname = ""
	lastname = ""
	email = ""
	avatar = ""
	error_in_signup_message = ""
	error_in_signup = OK

	if request.method == 'POST':
		signup_form = LoginForm(request.POST)

		if signup_form.is_valid():
			# comment = signup_form.cleaned_data["comment"]
			username = signup_form.cleaned_data["username"]
			password = signup_form.cleaned_data["password"]
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



def index(request):
    questions = list(QUESTIONS.values())
    template = loader.get_template('questions/index.html')
    
    
    current_page, paginator = paginate(questions, request)

    context = {
        'questions': current_page,
    }
    return HttpResponse(template.render(context, request))
