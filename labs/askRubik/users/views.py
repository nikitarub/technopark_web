from django.shortcuts import render
from questions.models import Tag, Question, Answer
from users.models import Profile

# TODO сделать обратботку ошибок: проверка совпадения паролей


def _sidebar_context(request):
    return {
        'popular_tags': Tag.objects.most_popular(),
        'best_members': Profile.objects.best_members(),
    }


# Create your views here.
def register(request):
    context = {
        'title': 'Registration'
    }
    context.update(_sidebar_context(request))
    return render(request, 'users/register.html', context)


def login(request):
    context = {
        'title': 'Login'
    }
    context.update(_sidebar_context(request))
    return render(request, 'users/login.html', context)


def settings(request):
    context = {
        'title': 'Settings'
    }
    context.update(_sidebar_context(request))
    return render(request, 'users/settings.html', context)