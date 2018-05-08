from django.db import models
from django.db.models import Count

class QuestionManager(models.Manager):
    def all_new(self):
        return self.order_by('-date').all()

    def all_rate(self):
        return self.order_by('-rating').all()

    def all_questions_by_tag(self, tag_name):
        return self.filter(tags=tag_name).all()


class AnswerManager(models.Manager):
    def all_answers_by_question(self, question_id):
        return self.filter(question__pk=question_id).all()


class TagManager(models.Manager):
    def with_question_count(self):
        return self.annotate(questions_count=Count('question'))

    def order_by_question_count(self):
        return self.with_question_count().order_by('-questions_count')

    def order_by_name_with_question_count(self):
        return self.with_question_count().order_by('text')

    def most_popular(self):
        return self.order_by_question_count().all()[:5]

class Tag(models.Model):
    objects = TagManager()
    name = models.CharField(max_length=30)



class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)


class Answer(models.Model):
    objects = AnswerManager()
    text = models.TextField()
    author = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    date_pub = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)










