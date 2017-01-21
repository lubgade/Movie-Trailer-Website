"""
Movie trailer website(integration with the movie database API)
Leena Ghanekar

"""

import tmdbsimple as tmdb  # import the library
import fresh_tomatoes
import media

tmdb.API_KEY = 'd63bc486789e992fa2fa497bfd2d4dcc'  # add your API KEY before executing this code
mymovies = []


def addresults(results):
    for movie in movies.results:
        movieid = movie['id']  # Retrieving movie id
        title = movie['title']  # Retrieving movie title
        overview = movie['overview']  # Retrieving the storyline
        poster_path = "https://image.tmdb.org/t/p/w300_and_h450_bestv2" + movie['poster_path']  # poster image url
        movieobj = tmdb.Movies(movieid)
        response = movieobj.videos()
        if len(movieobj.results) > 0:
            video = movieobj.results[0]
            url = "http://www." + video['site'] + ".com/watch?v=" + video['key']  # you tube url
        else:
            url = "https://www.youtube.com/watch?v=u5BMudMSXo0"  # if no url is available then assign default url
        mymovie = media.Movie(title, overview.encode('ascii', 'ignore'), poster_path, url)  # forming a Movie object
        mymovies.append(mymovie)  # appending object instances to a list


movies = tmdb.Movies()  # creating an instance of type Movies to communicate with the API
response = movies.upcoming()  # getting info on upcoming movies
addresults(movies.results)  # passing the info to form an object of type Movie to form a list of upcoming movies
fresh_tomatoes.open_movies_page(mymovies)  # passing the list of movies to generate an HTML

'''
response = movies.now_playing()  #getting info on currently playing movies
addresults(movies.results)
discover = tmdb.Discover()  #to discover movies from a particular year
response = discover.movie(page=1,year=2016)
pages = discover.total_pages
for i in range(1,20):
  discover.movie(page=i,year=2016)
  addresults(discover.results)
  print i
'''
