import webbrowser


# Define movie class.
class Movie():
    """ This class provides a way to store movie related information. """

    # Define object values.
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, rating, duration):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = rating
        self.duration = duration

    # Define show_trailer function.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
