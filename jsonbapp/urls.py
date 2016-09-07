from django.conf.urls import url

from . import views

app_name='jsonbapp'
urlpatterns=[
	url(r'^$',views.index,name='index'),	
	url(r'^save/$',views.save,name='save'),
]