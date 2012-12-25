Using the library
=================

python-omdb is in alpha stage. It currently only supports basic search.


Searching by title
------------------
::

	import omdb

	>>> omdb.search("Idiocracy")
	[{'Year': '2006', 'imdbID': 'tt0387808', 'Title': 'Idiocracy'}]

omdb.search() will return a list of dicts. Those dicts contain the data returned by the OMDb API.