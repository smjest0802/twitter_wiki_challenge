from django.shortcuts import render

from .forms import SearchForm

from django.http import HttpResponseRedirect

def IndexView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            search_text = form.cleaned_data['search_text']

            print search_text
            #return HttpResponseRedirect('/search/index.html', {'search_text': search_text})

            #from api.wiki_search import queryWiki
            from .api.wiki_search import queryWiki

            query_results = queryWiki(search_text)

            return render(request, 'search/index.html', {'form':form, 'search_text': search_text, 'query_results': query_results})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()


    return render(request, 'search/index.html', {'form':form})
