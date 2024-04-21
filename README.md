## Task 1
### Create the following 3 classes
- Book
- Collection
- BookStore

### Explanation

**Book**
The book class has 3 attributes
- Title
- Author
- Year (it was published in. This is an integer)

**Collection**
A collection has the following attributes
- The name of the collection (e.g fiction, poetry, manga etc)
- A list of all the books within the collection
	Example:
		Suppose you have a book called "Death Note". A user can add the book "Death Note" to a collection called "Manga"


**Book Store**
This is a class that stores 2 things
- A dictionary of all the books available
	- This means that you have to store all the books that EXISTS in the store in this dictionary. You should store it in such a way that the dictionary keeps track of the quantities of each copy.
		Example:
		If you have 2 copies of the book "Death Note", the dictionary should store the number of copies of "Death Note", in this case it's 2.
- A way to store all of  the collections in the book store. ***Decide if whether or not this list contains the collection object or the collection name!***
- An ```assignCollection(b, c)``` function, where ```b``` is the Book object being added and ```c``` is the collection. If the collection ***already*** exists in bookstore, then the book should just be added to that collection. Otherwise, add the collection to **Note that both book and collection are already created before hand**
	```
	c1 = Collection("Manga")
	b1 = Book("Death Note", "Tsugumi Ohba", 2003)
	b = BookStore()

	b.assignCollection(b1, c1) # Assigns Book b1 to Collection c1
	```


# Additional Tasks

1. Create a function in BookStore that returns the list of the collection names, as well as the number of books in that collection
2. Create a function that removes a book from a collection in BookStore. ***Important! The book was REMOVED from the collection but ISN'T removed from the overall bookstore stock!***

# Sample code

### Sample 1
*main.py*
```
#!/usr/bin/env python

### Necessary
from bookstore import *

### Creating a book

b1 = Book("Oregairu", "Wataru Watari", 2011)

print(b1)
```
Expected Output:
```
Name: Oregairu
Author: Wataru Watari
Year: 2011
```

### Sample 2
```
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

print(bookstore.getBooks())
print()
```

Expected output
```
Book name: Oregairu 1x
Book name: Death Note 1x

Collection name: Manga Collection - Manga
Name: Oregairu
Author: Wataru Watari
Year: 2011
Name: Death Note
Author: Tsugumi Ohba
Year: 2003
```
