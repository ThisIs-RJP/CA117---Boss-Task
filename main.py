#!/usr/bin/env python

### Necessary
from bookstore import *

### Creating a book

b1 = Book("Oregairu", "Wataru Watari", 2011)
b2 = Book("Death Note", "Tsugumi Ohba", 2003)

### Creating a collection 
c = Collection("Manga")

bookstore = BookStore()
### Assigning our books to the collection manga
bookstore.assignCollection(b1, c)
bookstore.assignCollection(b2, c)
bookstore.assignCollection(b2, c)

print("Printing all the books in our Book store and their quantities")
print(bookstore.getBooks())
# print("Printing the contents of our collections")
# print(bookstore.getCollections())
# print("\nPrinting the collection we have built")
# print(c)