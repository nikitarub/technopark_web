from django.urls import path
from . import views


urlpatterns = [
    path('', views.questions, name='questions'),
    # path('questions/<int:page_number>', views.questions, name='questions'),
    path('ask/', views.ask, name='ask'),
    # path('question/', views.one_question_page, name='one_question_page'),
    path('question/<int:id>', views.one_question_page, name='one_question_page'),
    # path('tag/', views.tag, name='tag'),
    path('tag/<slug:tag_name>', views.tag, name='tag'),
    path('hot/', views.hot, name='hot'),
    # path('hot/<int:page_number>', views.hot, name='hot')

]