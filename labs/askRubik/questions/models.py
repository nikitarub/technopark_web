from django.db import models
# Create your models here.

from datetime import datetime

from django.contrib.auth.models import AbstractUser
# from questions.models import User

# Create your models here.


def search_by_tag(object_list, tag):
	object_list_ret = []
	for object_item in object_list:
		for object_tag in object_item["tags"]:
			if tag == object_tag:
				object_list_ret.append(object_item)
				break
	return object_list_ret


def search_by_hot(object_list):
	object_list_ret = []
	for object_item in object_list:
		for object_tag in object_item["tags"]:
			if tag == object_tag:
				object_list_ret.append(object_item)
				break
	return object_list_ret






# Перенести в users/models
class User(AbstractUser):
	"""docstring for User"""
	upload = models.ImageField(upload_to = 'uploads/%Y/%m/%d/')



class Tag(models.Model):
	title = models.CharField(max_length=120, verbose_name=u"Заголовок тэга")

	def __str__(self):
		return self.title
	

class Question(models.Model):
	"""docstring for Question"""
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	title = models.CharField(max_length=120, verbose_name=u"Заголовок вопроса")
	text = models.TextField(verbose_name=u"Текст вопроса")

	create_date = models.DateTimeField(default=datetime.now, verbose_name=u"Время создания вопроса")

	is_active = models.BooleanField(default=True, verbose_name="Доступность поста")
	tags = models.ManyToManyField(Tag, blank=True)


