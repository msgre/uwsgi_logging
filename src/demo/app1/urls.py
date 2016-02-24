from django.conf.urls import url

from .views import home, subpage

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^1/$', subpage, name='subpage'),
]
