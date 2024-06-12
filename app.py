from flask import Flask, jsonify, request
from pymongo import MongoClient


app = Flask(__name__)



#client= MongoClient("20.166.154.71:27017")  
#client= MongoClient("python-flask-app-lb")
client = MongoClient("mongodb://mongodb:27017/")
#client = MongoClient("mongodb://localhost:27017/")
db = client.Bookstore
books_collection = db.books


@app.route('/books', methods=['POST'])
def create_book():
    book_data = request.json
    books_collection.insert_one(book_data)
    return jsonify(book_data), 201


@app.route('/books', methods=['GET'])
def read_books():
    books = list(books_collection.find({}, {'_id': 0}))
    return jsonify(books)


@app.route('/books/<isbn>', methods=['PUT'])
def update_book(isbn):
    update_data = request.json
    books_collection.update_one({'isbn': isbn}, {'$set': update_data})
    return jsonify(update_data)


@app.route('/books/<isbn>', methods=['DELETE'])
def delete_book(isbn):
    books_collection.delete_one({'isbn': isbn})
    return jsonify({'message': 'Book got deleted successfully!'})

#finally
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

