"""
.. module:: search/urls.com
   :platform: Unix
   :synopsis: Which views to call for the URL

.. moduleauthor:: Andrew Carter <andrew@invalid.com>


"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
]
