from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tag/<tag>', views.tag, name='tag'),
    path('ask/', views.ask, name='ask'),
    path('hot/', views.hot, name='hot'),

    
    # ex: /polls/5/
    # path('questions/<int:page_number>', views.questions, name='questions'),
    path('question/', views.detail, name='detail'),

    # path('question/', views.get_comment, name='get_comment'),
   
    # ex: /polls/5/results/
    # path('<int:question>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question>/vote/', views.vote, name='vote'),
]