import media
import fresh_tomatoes

# We are creating instances of class Movie
# one for each movie we will display in our website.
the_dark_knight = media.Movie("The Dark Knight",
                              "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY")

memento = media.Movie("Memento",
                      "https://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg",
                      "https://www.youtube.com/watch?v=zgd0-VttkmA")

dr_strangelove = media.Movie("Dr. Strangelove or: How I Learned to \
                             Stop Worrying and Love the Bomb",
                             "https://upload.wikimedia.org/wikipedia/en/e/e6/Dr._Strangelove_poster.jpg",
                             "https://www.youtube.com/watch?v=IE9CmX15PYA")

sixth_sense = media.Movie("The Sixth Sense",
                          "https://upload.wikimedia.org/wikipedia/en/6/66/The_sixth_sense.jpg",
                          "https://www.youtube.com/watch?v=lXO0he1WjYw")

back_to_the_future = media.Movie("Back to the Future",
                                 "https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg",
                                 "https://www.youtube.com/watch?v=qvsgGtivCgs")

the_room = media.Movie("The Room",
                       "https://upload.wikimedia.org/wikipedia/en/e/e1/TheRoomMovie.jpg",
                       "https://www.youtube.com/watch?v=EE6RQ8rC8hc")

# This creates the movie list required to
# run open_movies_page().
movie_list = [the_dark_knight, memento, dr_strangelove,
              sixth_sense, back_to_the_future, the_room]

# This function takes the movie list and
# creates the website.
fresh_tomatoes.open_movies_page(movie_list)


