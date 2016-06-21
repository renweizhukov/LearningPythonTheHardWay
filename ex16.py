#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CRTL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

# The truncate call is redundant since the file is opened with mode 'w'.
# print "Truncating the file. Goodbye!"
# target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file."

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
multiline = "{0!s}\n{1!s}\n{2!s}\n".format(line1, line2, line3)
target.write(multiline)

print "And finally, we close it."
target.close()