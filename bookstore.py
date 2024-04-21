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