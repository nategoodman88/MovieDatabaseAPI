# Import MySQL parameters from config so they stay private
from Config import user
from Config import password
from Config import host
from Config import database
# Import MySQL connector
import mysql.connector

# Set a connection equal to the parameters from above to be used in later code
connection = mysql.connector.connect(user = user, password = password, host = host, database = database)