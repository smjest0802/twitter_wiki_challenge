"""
.. module:: search/views.py
   :platform: Unix
   :synopsis: Generates the views for the search application

.. moduleauthor:: Shawn Meginley <shawn.meginley@gmail.com>
"""

from django.shortcuts import render

from .forms import SearchForm
from .api.query_apis import QueryAPIs 

def IndexView(request):
    """Handles the view for the landing page and the search results page"""

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            searchText = form.cleaned_data['search_text']

            #return HttpResponseRedirect('/search/index.html', {'search_text': search_text})

            queryAPIs = QueryAPIs()

            queryAPIs.queryWiki(searchText)
            queryAPIs.queryTwitter(searchText)

            return render(request, 'search/index.html', {'form':form, 'search_text': searchText, 'query_results': queryAPIs})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()


    return render(request, 'search/index.html', {'form':form, 'landing': True})
