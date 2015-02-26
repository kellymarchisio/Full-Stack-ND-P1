import webbrowser

# define movie class 
class Movie():
	def __init__(self, title, poster, trailer):
		self.title = title
		self.poster_image_url = poster
		self.trailer_youtube_url = trailer

	def playTrailer(self):
		webbrowser.open(self.trailer_youtube_url)
