# Movie Database API


*Currently taken offline due to AWS costs


A Flask API application to interfact with a MySQL Database filled with the Blu Rays I own

Database is hosted on AWS RDS

API is hosted with AWS Elastic Beanstalk

This API can be used in the browser but it easiest in something like Postman

# Commands

# http://moviedatabaseapi-env.eba-drt3mnpz.us-east-2.elasticbeanstalk.com/

The base of the API, returns the titles of all the blu rays in the database

# http://moviedatabaseapi-env.eba-drt3mnpz.us-east-2.elasticbeanstalk.com/total

Returns the toal count of the titles in the database

# http://moviedatabaseapi-env.eba-drt3mnpz.us-east-2.elasticbeanstalk.com/imdbsearch?name="your name here minus quotes"

Returns either:
A. search of the movie title on IMDB using IMDB's API
B. a message that the title is not among the ones in the database

# http://moviedatabaseapi-env.eba-drt3mnpz.us-east-2.elasticbeanstalk.com/websearch?name="your name here minus quotes"

Returns either:
A. search of the movie title using Duck Duck Go 
B. a message that the title is not among the ones in the database

