'''

Movie Trailer Website
Leena Ghanekar

Main module :
1. Creates various instances of the object type Movie.
2. Creates a list of the Movie objects.
3. Passes the list to a html generator module(fresh_tomatoes.py)to generate
static content.

'''


#Dependencies
import fresh_tomatoes
import media

#Creating instances of the Movie object
toy_story = media.Movie("Toy Story",
                        "A story of a boy & his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar",
                     "A marine in an alien land",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

inception = media.Movie("Inception",
                        "When what you dream is the reality",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")


the_notebook = media.Movie("The Notebook",
                           "A love story",
                           "https://upload.wikimedia.org/wikipedia/en/8/86/Posternotebook.jpg",
                           "https://www.youtube.com/watch?v=FC6biTjEyZw")

special_26 = media.Movie("Special 26",
                         "Heist crime thriller",
                         "https://upload.wikimedia.org/wikipedia/en/7/7c/Special_26_poster.jpg",
                         "https://www.youtube.com/watch?v=DNi8nyn-v0s")

ratatouille = media.Movie("Ratatouille",
                          "A rat who can cook",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")


#Creating a list of the Movie objects
movies = [toy_story,avatar,inception,the_notebook,special_26,ratatouille]


#Passing the list of movies to generate an html
fresh_tomatoes.open_movies_page(movies)







                         
