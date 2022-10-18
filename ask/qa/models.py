from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
  def new(self):
    return self.order_by('-added_at')
  def popular(self):
    return self.order_by('-rating')
  
class Question(models.Model):
  objects = QuestionManager()
  title =  models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateTimeField(auto_now_add=True)
  rating = models.IntegerField(default=0)
  likes = models.ManyToManyField(User, related_name='question_like_user')
  author = models.ForeignKey(User, on_delete=models.CASCADE)

class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  user, _ = User.objects.get_or_create(                                   
            username='x',                                                       
            defaults={'password':'y', 'last_login': timezone.now()})
  question = Question(title='qwe', text='qwe', author=user)
