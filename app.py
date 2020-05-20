'''
import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['students']

students = [student for student in collection.find({})]

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['posts']

posts = [post for post in collection.find({})]
print(posts)
'''
from database import Database
from menu import Menu

Database.initialize()

menu = Menu()

menu.run_menu()
