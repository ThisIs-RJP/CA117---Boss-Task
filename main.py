#!/usr/bin/env python

### Necessary
from bookstore import *

### Creating a book

b1 = Book("Oregairu", "Wataru Watari", 2011)
b2 = Book("Death Note", "Tsugumi Ohba", 2003)
b3 = Book("I want to eat your pancreas", "Yoru Sumino", 2018)

### Creating a collection 
c = Collection("Manga")
c2 = Collection("Fiction")

bookstore = BookStore()
### Assigning our books to the collection manga
bookstore.assignCollection(b1, c)
bookstore.assignCollection(b2, c)
bookstore.assignCollection(b3, c2)

# print("Printing all the books in our Book store and their quantities")
# print(bookstore.getBooks())
# print("Printing the contents of our collections")
# print(bookstore.getCollections())
print("Printing the collection we have built")
print("This is our collection - {}".format(c))
print("This is our collection - {}".format(c2))