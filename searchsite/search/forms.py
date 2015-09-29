"""
.. module:: search/forms.py
   :platform: Unix
   :synopsis: Specification of the forms for the search application

.. moduleauthor:: Shawn Meginley <shawn.meginley@gmail.com>


"""
from django import forms

class SearchForm(forms.Form):
    search_text = forms.CharField(label='Topic', max_length=100)
