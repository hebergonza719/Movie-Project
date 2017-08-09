class Movie():
    '''
    This class creates instances of movies and stores properties
    of the movies to be displayed, such as the title,
    the movie poster and youtube trailer.
    '''
    def __init__(self, movie_title, poster_image, trailer_youtube):
        # This initializes an instance of the class Movie and its variables.
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    
