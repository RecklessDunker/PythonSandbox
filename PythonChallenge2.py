
# --------------------------------------------------------
# Author: James Griffiths
# Date Created: Saturday, 29th June 2019
# Version: 1.0
# --------------------------------------------------------

# Challenge Three ----------------------------------------

# Description: http://www.pythonchallenge.com/pc/def/ocr.html
# Looks like I need to strip out 'rare characters' from the source code on the web page. Maybe.
#
# Pseudo Code:
# turn the code into a list
# loop through the individual characters in the list add them as a key in a dict
# count the occurrences of that character in the list and add that as the key value pair
# repeat until end of list

# Open a file to read from...
file = open("/Users/jim/Google Drive/Dev Team/Jim/GitHub/Challenge2.txt", "r")

# create a dictionary where I'll strip out each character as a key and give the paired value it's occurrence count

# reads and prints out all the lines as one line then strips out individual chars for the dictionary
lines = file.readlines()
indchars = '\t'.join([line.strip() for line in lines])
# create a dictionary to store characters as keys and occurrences as value pairs
d = {}
# iterate over each character, add it as a key and add a count value for every same character in the list
for char in indchars:
    d[char] = d.get(char, 0) + 1
# now get the characters that have a count value of 1 and join them together to make a word
print("".join(ch for ch in indchars if d[ch] == 1))

