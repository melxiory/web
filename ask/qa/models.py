from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
  def new(self):
    return self.order_by('-added_at')
  def popular(self):
    return self.order_by('-rating')
  
added_at = models.DateTimeField(auto_now_add=True)
rating = models.IntegerField(default=0)
likes = models.ManyToManyField(User, related_name='question_like_user')
author = models.ForeignKey(User, on_delete=models.CASCADE)
# Create your models here.
