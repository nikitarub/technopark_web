from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class ProfileManager(models.Manager):
    def create_user(self, username, email, password, avatar, nickname):
        user = User.objects.create_user(username, email, password)
        return self.create(user=user, avatar=avatar, nickname=nickname)

    def best_members(self):
        pass


class Profile(models.Model):
    objects = ProfileManager()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField()
    nickname = models.CharField(max_length=100)

    def login(self):
        return self.user.username

    def email(self):
        return self.user.email

    def password(self):
        return self.user.password

    def image_url(self):
        return '/static/img/smile.png'