# Imports generated from method calls
from unittest import result
# Import the previously created MySQL connection from seperate file
from MySQLConnect import connection
# Import flask so the information can be viewed via API
from flask import Flask, request
from flask_restful import Resource, Api
# Import IMDBPy from Github to allow searching the IMDB database for the movies by title
import imdb
# Import Duck Duck Go to allow a web search for the movie 
from duckduckgo_search import ddg

# create IMDB instance 
moviesearcher = imdb.IMDb()
# Flask API name is equal to this file
app = Flask(__name__)
api = Api(app)
# Everything below here is public as it may be used in multiple get requests 

# Set empty array to later store the movies titles into
movieTitleArr = []
# Set a query to get all the data from the titles table. The are two columns in the table: movie ID and movie name
selectQuery = 'select * from Titles'
cursor = connection.cursor()
cursor.execute(selectQuery)
# Variable movies is equal to the results from above
movies = cursor.fetchall()
# Variable rows is equal to the number of rows in the table 
rows = cursor.rowcount
# For loop that populates the movie array with the movie information pulled from the database
for rows in movies:
    movieTitleArr.append(rows[1])
# Set empty var to count the movie total
movieCount = 0
# For loop that populates the previously created array with the movie information pulled from the database
for rows in movies:
    movieCount += 1

# Class with function to get the list of the movies from the database
class movieList(Resource):
    def get(self):
        # Returns movie title array
        return {'titles of blurays owned': movieTitleArr}, 200
# Class with function to get the total count of the movies owned
class movieTotal(Resource):
    def get(self):
        # Return total movies
        return {'total blurays owned' : movieCount}, 200
# Class with function to search IMDB for a specific movie from the ones in the database
class imdbsearch(Resource):
    def get(self):
        name = request.args.get('name')
        if name not in movieTitleArr:
            return 'bluray not owned but no HTTP error'
        else:
            search = moviesearcher._search_movie(name, result)
            return {'movie searched': search}, 200
# Class to web search for one of the movies using Duck Duck Go
class websearchMovie(Resource):
    def get(self):
        name = request.args.get('name')
        if name not in movieTitleArr:
            return 'bluray not owned but no HTTP error'
        else:
            keyword = name
            results = ddg(keyword, region='wt=wt', safesearch='Moderate', time= None, max_results= 5)
            return {'movie searched' : results}, 200

# Add the class as a resource to the API and the route
api.add_resource(movieList, '/')
api.add_resource(movieTotal, '/total')
api.add_resource(imdbsearch, '/imdbsearch')
api.add_resource(websearchMovie, '/websearch')

# Call debug if ran from console
if __name__ == '__main__':
    app.run(debug=True)
