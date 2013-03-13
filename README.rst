Using the library
=================

python-omdb is in alpha stage. It currently only supports basic search.


Searching by title
------------------
::

	import omdb

	>>> results = omdb.search("Idiocracy")
	[Movie,Movie,...]
	>>> print results[0].title
	Idocracy



omdb.search() will return a list of dicts. Those dicts contain Movie objects, containing all the information found from that movie. See source.