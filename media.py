import webbrowser
# Class Movie which has the movie title, storeline, poster image and youtube trailer
class Movie():
  """ This class provides a way to store movie related information"""
  VALID_RATINGS = ["G", "PG", "Pg-13", "R"]
  #Sets the title, storyline, poster image and youtube trailer
  def __init__(self, movie_title, movie_storyline, poster_image,
  trailer_youtube):
      self.title = movie_title
      self.storyline = movie_storyline
      self.poster_image_url = poster_image
      self.trailer_youtube_url = trailer_youtube
  #this function opens the trailer from youtube 
  def show_trailer(self):
      webbrowser.open(self.trailer_youtube_url)
