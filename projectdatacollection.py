import requests_with_caching
import json

def get_movies_from_tastedive(querystring):
    baseurl="https://tastedive.com/api/similar"
    params_diction = {}
    params_diction['q']=querystring
    params_diction['type']='movies'
    params_diction['limit']="5"
    testdive_resp=requests_with_caching.get(baseurl, params = params_diction)
    print(testdive_resp.url)
    return testdive_resp.json()
def extract_movie_titles(querydict):
    movietitles=[]
    for key in querydict['Similar']['Results'][:]:
        #print(key['Name'])
        movietitles.append(key['Name'])
    return movietitles


def get_related_titles(listofmovies):
    newlist=[]
    for eachmovie in listofmovies:
        elem=extract_movie_titles(get_movies_from_tastedive(eachmovie))
        for ele in elem:
            if ele not in newlist:
                newlist.append(ele)
    return newlist
def get_movie_data(movietitle):
    paradict = {'t': movietitle, 'r': 'json'}
    omdbapi_response = requests_with_caching.get('http://www.omdbapi.com/', params=paradict)
    return omdbapi_response.json()

def get_movie_rating(moviedict):
    if len(moviedict['Ratings']) > 1:
        if moviedict['Ratings'][1]['Source'] == 'Rotten Tomatoes':
            rottenvalue = moviedict['Ratings'][1]['Value'][:2]
            rottenvalue = int(rottenvalue)
    else:
        rottenvalue = 0

    return rottenvalue
def get_sorted_recommendations(listMovieTitle):
    listMovie= get_related_titles(listMovieTitle)
    listMovie= sorted(listMovie, key = lambda movieName: (get_movie_rating(get_movie_data(movieName)), movieName), reverse=True)

    return listMovie
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"]))

import requests_with_caching
import json

def get_movies_from_tastedive(querystring):
    baseurl="https://tastedive.com/api/similar"
    params_diction = {}
    params_diction['q']=querystring
    params_diction['type']='movies'
    params_diction['limit']="5"
    testdive_resp=requests_with_caching.get(baseurl, params = params_diction)
    print(testdive_resp.url)
    return testdive_resp.json()
def extract_movie_titles(querydict):
    movietitles=[]
    for key in querydict['Similar']['Results'][:]:
        #print(key['Name'])
        movietitles.append(key['Name'])
    return movietitles


def get_related_titles(listofmovies):
    newlist=[]
    for eachmovie in listofmovies:
        elem=extract_movie_titles(get_movies_from_tastedive(eachmovie))
        for ele in elem:
            if ele not in newlist:
                newlist.append(ele)
    return newlist
def get_movie_data(movietitle):
    paradict = {'t': movietitle, 'r': 'json'}
    omdbapi_response = requests_with_caching.get('http://www.omdbapi.com/', params=paradict)
    return omdbapi_response.json()

def get_movie_rating(moviedict):
    if len(moviedict['Ratings']) > 1:
        if moviedict['Ratings'][1]['Source'] == 'Rotten Tomatoes':
            rottenvalue = moviedict['Ratings'][1]['Value'][:2]
            rottenvalue = int(rottenvalue)
    else:
        rottenvalue = 0

    return rottenvalue
def get_sorted_recommendations(listMovieTitle):
    listMovie= get_related_titles(listMovieTitle)
    listMovie= sorted(listMovie, key = lambda movieName: (get_movie_rating(get_movie_data(movieName)), movieName), reverse=True)

    return listMovie
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"]))
