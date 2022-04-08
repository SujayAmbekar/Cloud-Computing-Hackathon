from pymongo import MongoClient
from datetime import datetime

# username as set for the mongodb admin server (the username used in secret.yaml - before base64 conversion)
user = 'testUser'
# password as set for the mongodb admin server (the password used in secret.yaml - before base64 conversion)
password = 'testPassword'
# service name of the mongodb admin server as set in the service for mongodb server
host = 'mongodb-service'
# port number of the mongodb admin server as set in the service for mongodb server
port = '27017'
conn_string = f'mongodb://{user}:{password}@{host}:{port}/?authSource=admin'

db = MongoClient(conn_string).blog


def addRecord(title, author, createdAt):
    # save the record to the database
    db.posts.insert_one(
        {"title": title, "author": author, "createdAt": createdAt})


posts = [
    {'title': 'Blog 1',
    'author': 'Sujay',
    'createdAt': datetime.fromtimestamp(1648708451)},
    {'title': 'Blog 2',
    'author': 'Sumukh',
    'createdAt': datetime.fromtimestamp(1648708151)},
    {'title': 'Blog 3',
    'author': 'Suhail',
    'createdAt': datetime.fromtimestamp(1648707451)},
    {'title': 'Blog 4',
    'author': 'Sucheth',
    'createdAt': datetime.fromtimestamp(1648709451)}
]

for post in posts:
    addRecord(post['title'], post['author'], post['createdAt'])

print("Records added successfully")
