from django.contrib import admin

# Register your models here.

from questions.models import Question, User, Tag


admin.site.register(Question)
admin.site.register(User)
admin.site.register(Tag)
