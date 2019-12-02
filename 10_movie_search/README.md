# App 10: Movie Search App


Key concepts introduced
=================

**The API**

You can find the details of the JSON HTTP API at [movie_service.talkpython.fm](http://movie_service.talkpython.fm/).

**Try/Except Error Handling**

    try:
        method1()
        method2()
        method3()
    except ConnectionError as ce:
        # handle network error
    except Exception as x:
        # handle general error

**Raising your own errors and exceptions**

    class MovieClient:
        def __init__(self, search_text):

            if not search_text or not search_text.strip():
                raise ValueError('Must specify a search string.')