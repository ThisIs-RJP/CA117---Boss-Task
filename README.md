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
- A list of all the collections in the book store. ***Decide if whether or not this list contains the collection object or the collection name!*** Although the solution I have in mind doesn't involve dictionaries, you may solve this problem using a dictionary.
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
