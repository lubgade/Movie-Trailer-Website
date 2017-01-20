# Movie-Trailer-Website


## Overview

A basic movie trailer website created with Python, in partial fulfilment of the Udacity [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## Prerequisites

Requires Python 2.7.12, Ubuntu 16.04 and IDLE(optional, typically installed as a part of Python install).
This code has been tested on Ubuntu 16.04 but should work on Windows/Mac OS with Python 2.7.12.
Optional - To use the API integration install tmdbsimple

## Installation

To install Python On Ubuntu, run from terminal `sudo apt install python`. Alternatively [download](https://www.python.org/downloads/) Python from the Python website. Instructions for installation are on the website.
Once Python is installed, to use this application/code a user can fork this repository, download a .zip archive & unzip or if git is already installed from terminal   
`git clone https://github.com/lubgade/Movie-Trailer-Website`.  
(To install git from terminal `sudo apt install git`).   

#### Optional - 
* To install tmdbsimple `sudo pip install tmdbsimple`(To install pip - `sudo apt install python-pip`). 
* Register to [the movie database](https://www.themoviedb.org/account/signup) and generate an API Key.

## Usage

To run the application, open `entertainment_center.py` module or the `movie_center.py` module using IDLE or from terminal    
`python entertainment_center.py` or `python movie_center.py`. This will generate a `Movie Trailers.html` file in the browser. Each time the user runs this application, the `Movie Trailers.html` file will be overwritten.

#### Modules

* `entertainment_center.py` - the core module, that imports the other two. Creates a list of movies then passes it to the `fresh_tomatoes.py` module to output static content. 
* `media.py` - used by the `entertainment_center.py` module. This is the blueprint for creating instances of the `Movie` object with different properties.
* `fresh_tomatoes.py` - used by `entertainment_center.py` module to generate static HTML page from a list of movies.
* `movie_center.py` - an extra module which integrates with [the movie database API](https://www.themoviedb.org/documentation/api) to generate an HTML page for upcoming movies.

#### Properties of the class Movie

* `title` - the movie title
* `storyline` - the storyline of the movie
* `poster_image_url` - url of the poster image
* `trailer_youtube_url` - url of the youtube video for the movie

#### Example of an instance of the class Movie

```python
special_26 = media.Movie("Special 26",
                         "Heist crime thriller",
                         "https://upload.wikimedia.org/wikipedia/en/7/7c/Special_26_poster.jpg",
                         "https://www.youtube.com/watch?v=DNi8nyn-v0s")
```                         

## Extras

* `fresh_tomatoes.py` modified to include tooltip using bootstrap to show the `storyline` for each movie
*  `movie_center.py` integrates with the movie database API to generate an HTML page for upcoming movies.
                         





