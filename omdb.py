import json
from urllib.parse import quote
from urllib.request import urlopen


API_URL = "http://www.omdbapi.com/?r=json&s=%s"

class APIError(Exception):
	pass

def search(title):
	title = title.encode("utf-8")
	url = API_URL % quote(title)
	data = urlopen(url).read().decode("utf-8")
	data = json.loads(data)
	if data.get("Response") == "False":
		raise APIError(data.get("Error", "Unknown error"))

	return data.get("Search", [])
