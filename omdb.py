__version___ = "0.1"

import json
try:
	from urllib.parse import quote
except:
	from urllib import quote
try:
	from urllib.request import urlopen
except:
	from urllib2 import urlopen

class APIUrls(object):
	search = "http://www.omdbapi.com/?r=json&s=%s"
	imdbid = "http://www.omdbapi.com/?r=json&i=%s"
	title  = "http://www.omdbapi.com/?r=json&t=%s"
	titleYear = "http://www.omdbapi.com/?r=json&t=%s,y=%s"

class APIError(Exception):
	pass
def getUrl(url):
	data = urlopen(url.encode("utf-8")).read().decode("utf-8")
	return json.loads(data)

class Movie(object):
	def __init__(self,jsonData):
		print jsonData
		self.rawData = jsonData
		if "Response" not in self.rawData:
			self.rawData = getUrl(APIUrls.imdbid % quote(self.rawData['imdbID']))

		self.Title = self.rawData.get("Title")
		self.Year = self.rawData.get("Year")
		self.Rated = self.rawData.get("Rated")
		self.Released = self.rawData.get("Released")
		self.Runtime = self.rawData.get("Runtime")
		self.Genre = self.rawData.get("Genre")
		self.Director = self.rawData.get("Director")
		self.Writer = self.rawData.get("Writer")
		self.Actors = self.rawData.get("Actors")
		self.Plot = self.rawData.get("Plot")
		self.Poster = self.rawData.get("Poster")
		self.imdbRanking = self.rawData.get("imdbRanking")
		self.imdbVotes = self.rawData.get("imdbVotes")
		self.imdbID = self.rawData.get("imdbID")
		self.Type = self.rawData.get("Type")

def search(title):
	url = APIUrls.search % quote(title)
	data = getUrl(url)

	if data.get("Response") == "False":
		raise APIError(data.get("Error", "Unknown error"))
	result = []
	for m in data["Search"]:
		result.append(Movie(m))

	return result

if __name__ == "__main__":
	for movie in search("The Girl With The Dragon Tattoo"):
		print movie.rawData