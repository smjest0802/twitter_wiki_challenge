# twitter_wiki_challenge
This is a small Django project (`searchsite`) with a single application called `search` that searches Twitter and Wiki. The project presents a user with a prompt for a topic to search for. The first 10 results from Wiki and first 5 results from Twitter are displayed.



Need to install:

```
$ pip install python-twitter
```

How to start application:

```
cd <location of pull>/twitter_wiki_challenge/searchsite
$ python manage.py runserver
```

Useful links:
- <https://github.com/bear/python-twitter>(Description of Twitter Python API used)
- <https://www.mediawiki.org/wiki/API:Main_page>(Wiki API documentation)

# Performance Profile
The initial search page loads in 15ms. The page loads in around 800ms after the search for a topic is started. About 400ms of this is spent pulling the results from the Wiki and parsing the results and about 250ms is spent pulling the Twitter results and parsing them. The page is currently hosted on a Dell Inspiron reaching out the internet via Wifi on my home network.

To increase the performance I would run through trying the following:
- Make the connection wired instead of wireless.
- Do some speed tests to the api website to determine latency just for that.
- Run the APIs on seperate CPUs to ensure they are running in parrallel.
- Look at caching results for a period of time.
