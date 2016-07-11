import fresh_tomatoes
import media

# Initialize movie object data.
ninja_protector = media.Movie("Ninja: The Protector", "Only a ninja can defeat a ninja.",
                              # This is the poster link.
                              "http://ia.media-imdb.com/images/M/MV5BMTkzNjE0Njc1MV5BMl5BanBnXkFtZTYwOTIyNjI5._V1_.jpg",
                              # This is the trailer link.
                              "http://www.youtube.com/watch?v=scs0vs1smfc",
                              # This is the movie's rating.
                              "R",
                              # This is the movie's duration in minutes.
                              92)

chud_ii = media.Movie("CHUD II: Bud the CHUD", "He's hot! He's sexy! He's dead!",
                      "http://ia.media-imdb.com/images/M/MV5BMTM3NTU3NTU4OF5BMl5BanBnXkFtZTcwMjU0MTMyMQ@@._V1_.jpg",
                      "http://www.youtube.com/watch?v=Nv1_Ig58V2Y",
                      "R",
                      84)

troll_ii = media.Movie("Troll II", "One was not enough!",
                       "http://ia.media-imdb.com/images/M/MV5BMTg1ODgyNDYwM15BMl5BanBnXkFtZTcwNjYxNDY3NA@@._V1_.jpg",
                       "http://www.youtube.com/watch?v=GO6JVBygYxQ",
                       "PG-13",
                       95)

rubin_and_ed = media.Movie("Rubin and Ed", "As soon as Ed saves Rubin's life, he's gonna kill him.",
                           "http://ia.media-imdb.com/images/M/MV5BMTc2NjMwODE1M15BMl5BanBnXkFtZTcwMDYxOTAwMQ@@._V1_.jpg",
                           "http://www.youtube.com/watch?v=Ltjw-LiwOiQ",
                           "PG-13",
                           82)

the_room = media.Movie("The Room", "Can you really trust anyone?",
                       "http://ia.media-imdb.com/images/M/MV5BMTg4MTU1MzgwOV5BMl5BanBnXkFtZTcwNjM1MTAwMQ@@._V1_.jpg",
                       "http://www.youtube.com/watch?v=yCj8sPCWfUw",
                       "R",
                       99)

space_truckers = media.Movie("Space Truckers", "Earth's only hope.",
                             "http://ia.media-imdb.com/images/M/MV5BNzgwMjc0Njk4MV5BMl5BanBnXkFtZTgwNTA5MjgwMzE@._V1_.jpg",
                             "http://www.youtube.com/watch?v=EgdeaHr5LT0",
                             "PG-13",
                             95)

# Put the movies into an array.
movies = [rubin_and_ed, ninja_protector,
          chud_ii, troll_ii, the_room, space_truckers]

# Call the page generator with the movies array.
fresh_tomatoes.open_movies_page(movies)
