"""
.. module:: urls.py
   :platform: Unix
   :synopsis: Valid URLs for the application

.. moduleauthor:: Shawn Meginley <shawn.meginley@gmail.com>
"""

from django.conf.urls import include, url

urlpatterns = [
    url(r'^search/(index.html)?', include('search.urls', namespace='search')),
]
