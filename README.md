## Python-Data-Collection-and-Processing-Course-Project
Final Project of the Data Collection and Processing with Python. This course is part of the Python 3 Programming Specialization offer by University of Michigan in Coursera. You can find more information at https://www.coursera.org/learn/data-collection-processing-python/home/welcome
# About it
This project will take you through the process of mashing up data from two different APIs to make movie recommendations. The TasteDive API lets you provide a movie (or bands, TV shows, etc.) as a query input, and returns a set of related items. The OMDB API lets you provide a movie title as a query input and get back data about the movie, including scores from various review sites (Rotten Tomatoes, IMDB, etc.).

You will put those two together. You will use TasteDive to get related movies for a whole list of titles. You’ll combine the resulting lists of related movies, and sort them according to their Rotten Tomatoes scores (which will require making API calls to the OMDB API.)
To avoid problems with rate limits and site accessibility, we have provided a cache file with results for all the queries you need to make to both OMDB and TasteDive. Just use requests_with_caching.get() rather than requests.get(). If you’re having trouble, you may not be formatting your queries properly, or you may not be asking for data that exists in our cache. We will try to provide as much information as we can to help guide you to form queries for which data exists in the cache.
The documentation for the API is at https://tastedive.com/read/api.

The documentation for the API is at https://www.omdbapi.com/

# functions
1. def get_movies_from_tastedive(querystring):
It should take one input parameter, a string that is the name of a movie or music artist. The function should return the 5 TasteDive results that are associated with that string; be sure to only get movies, not other kinds of media. It will be a python dictionary with just one key, ‘Similar’.

2. def extract_movie_titles(querydict):
It extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive. Call it extract_movie_titles.

3. def get_related_titles(listofmovies):
It takes a list of movie titles as input. It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all into a single list. Doesn't include the same movie twice.

4. def get_movie_data(movietitle):
It takes in one parameter which is a string that should represent the title of a movie you want to search. The function should return a dictionary with information about that movie.

5. def get_movie_rating(moviedict):
It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer. If there is no Rotten Tomatoes rating, return 0.

6. get_sorted_recommendations(listMovieTitle):
It takes a list of movie titles as an input. It returns a sorted list of related movie titles as output, up to five related movies for each input movie title. The movies should be sorted in descending order by their Rotten Tomatoes rating, as returned by the get_movie_rating function. Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.

Note: This project was specifically completed in runestone environment for the mentioned MOOC, as such using the module "requests_with_caching" only available in runestone environment. 

Authors/authors:
Emon Sarkar

Course material: University of Michigan in Coursera. You can find more information at https://www.coursera.org/learn/data-collection-processing-python/home/welcome
