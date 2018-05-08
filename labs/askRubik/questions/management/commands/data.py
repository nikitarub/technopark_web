from random import choice, randint
from faker import Factory
from django.contrib.auth.models import User
from django.core.management import BaseCommand
import os
from questions.models import Tag, Question, Answer
from users.models import Profile


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.fill_questions()
        self.fill_answers()
        self.fill_tags_questions()


    def fill_questions(self):
        fake = Factory.create()



        starts = (
                'How do I Sort a Multidimensional',
                'What is Max?',
                'SQL Server'
                )

        for i in range(0, 40):
            q = Question()

            q.title = fake.sentence(nb_words=randint(2, 4), variable_nb_words=True)
            q.text = u"%s %s %s" % (
                    choice(starts),
                    os.linesep,
                    fake.paragraph(nb_sentences=randint(1, 4), variable_nb_sentences=True),
                    )
            q.author = Profile.objects.first()
            q.rating = randint(0, 1500)
            q.id = i
            q.save()
            self.stdout.write('add question [%d]' % (q.id))


    def fill_answers(self):
        fake = Factory.create()

        min_number = 10
        max_number = 20


        questions = Question.objects.all()
        is_correct = (True, False)
        counter = 1
        for q in questions:
            for i in range(0, randint(min_number, max_number)):
                ans = Answer()

                ans.text = fake.paragraph(nb_sentences=randint(2, 4), variable_nb_sentences=True)
                ans.author = Profile.objects.first()
                ans.question = q
                ans.rating = randint(0, 1500)
                ans.is_correct = choice(is_correct)
                ans.id = counter
                counter += 1
                ans.save()
                self.stdout.write('in question [%d] add ans [%d]' % (q.id, ans.id))


    def fill_tags_questions(self):
        tags = [
            'JavaScript', 'Java', 'Django', 'Nginx', 'Gunicorn', 'php', 'Android', 'Jquery', 'Python',
            'HTML', 'CSS', 'ios', 'MySQL', 'Windows', 'Docker'
        ]

        for tag in tags:
            if len(Tag.objects.filter(name=tag)) == 0:
                t = Tag()
                t.name = tag
                t.save()

        number = 10

        tags = Tag.objects.all()

        questions = Question.objects.all()

        for q in questions:
            if len(q.tags.all()) < number:
                for i in range(0, number - len(q.tags.all())):
                    t = choice(tags)

                    if t not in q.tags.all():
                        q.tags.add(t)
                        q.save()
            self.stdout.write('in question [%d] add tags' % q.id)
