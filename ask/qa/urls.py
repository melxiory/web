from django.conf.urls import url
from qa.views import test

urlpatterns = [ 
  url(r'^', main), 
  url(r'^question/\d+/$', question)
  url(r'^popular/.*$', popular)
]
