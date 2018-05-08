from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from questions.models import Tag, Question, Answer
from users.models import Profile

def _paginate(objects_list, request):
    objects_page = []

    paginator = Paginator(objects_list, 10)
    page = request.GET.get('page')
    try:
        objects_page = paginator.page(page)
    except PageNotAnInteger:
        objects_page = paginator.page(1)
    except EmptyPage:
        page = int(page)
        if page < 1:
            objects_page = paginator.page(1)
        elif page > paginator.num_pages:
            objects_page = paginator.page(paginator.num_pages)

    return objects_page



def _sidebar_context(request):
    return {
        'popular_tags': Tag.objects.most_popular(),
        'best_members': Profile.objects.best_members(),
    }

def questions(request):
    context = {
        'questions': _paginate(Question.objects.all_new(), request)
    }
    context.update(_sidebar_context(request))
    return render(request, 'questions/index.html', context)



def one_question_page(request, id):
    question = get_object_or_404(Question, pk=id)
    comments = _paginate(Answer.objects.all_answers_by_question(id), request)
    context = {
        'question': question,
        'comments': comments
    }
    context.update(_sidebar_context(request))
    return render(request, 'questions/question.html', context)


def tag(request, tag_name):

    tag = Tag.objects.get(name=tag_name)
    context = {
        'tag': tag,
        'questions': _paginate(Question.objects.all_questions_by_tag(tag_name), request)
    }

    context.update(_sidebar_context(request))
    return render(request, 'questions/tag.html', context)


def hot(request):
    context = {
        'questions': _paginate(Question.objects.all_rate(), request),
    }
    context.update(_sidebar_context(request))
    return render(request, 'questions/hot.html', context)


def ask(request):
    context = {
        'title': 'New question'
    }
    context.update(_sidebar_context(request))
    return render(request, 'questions/ask.html', context)
