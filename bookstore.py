#!/usr/bin/env python

class Book(object):

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        output = []

        output.append("Name: {}".format(self.title))
        output.append("Author: {}".format(self.author))
        output.append("Year: {}".format(self.year))

        return "\n".join(output)
    
class Collection(object):

    def __init__(self, name):
        self.name = name
        self.collection = []

    
    def addBook(self, book):
        self.collection.append(book)

    def __str__(self):
        output = []

        output.append("Collection - {}".format(self.name))
        for book in self.collection:
            output.append(str(book))
        
        return "\n".join(output)
    
class BookStore(object):

    def __init__(self):
        self.allbooks = {} ### Key type: String, Value type: int
        self.collections = {} ### Key type: String, Value type: Collection Object

    def assignCollection(self, book, collection):

        if book.title not in collection.collection: # if book is not in that collection, go ahead and add it
            collection.addBook(book)
        
        if book.title in self.allbooks:
            self.allbooks[book.title] += 1
        else:
            self.allbooks[book.title] = 1

        if collection.name not in self.collections: ## Adding it to collections if the collection name doesnt exist yet
            # self.collections.addBook(collection.name)
            self.collections[collection.name] = collection

    def getBooks(self): ## Outputs all the books in our book store
        output = []
        for k,v in self.allbooks.items():
            output.append("Book name: {} {}x".format(k, v))

        return "\n".join(output)

    def getCollections(self):
        output = []

        for k, v in self.collections.items():
            output.append("Collection name: {} {}".format(k, str(v)))
        
        return "\n".join(output)