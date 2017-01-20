import tmdbsimple as tmdb
import fresh_tomatoes
import media
tmdb.API_KEY = ''  #add your API KEY before executing this code
mymovies = []

def addresults (results):
    for movie in movies.results:
        movieid = movie['id']
        title = movie['title']
        overview = movie['overview']
        poster_path = "https://image.tmdb.org/t/p/w300_and_h450_bestv2" + movie['poster_path']
        movieobj = tmdb.Movies(movieid)
        response = movieobj.videos()

        for video in movieobj.results:
            url = "http://www." + video['site'] + ".com/watch?v=" + video['key']
        mymovie = media.Movie(title,overview.encode('ascii','ignore'),poster_path, url)
        mymovies.append(mymovie)

movies = tmdb.Movies()
response = movies.top_rated()
addresults(movies.results)
'''
response = movies.upcoming()
addresults(movies.results)
discover = tmdb.Discover()
response = discover.movie(page=1,year=2016)
pages = discover.total_pages
for i in range(1,20):
  discover.movie(page=i,year=2016)
  addresults(discover.results)
  print i
'''
fresh_tomatoes.open_movies_page(mymovies)


    
