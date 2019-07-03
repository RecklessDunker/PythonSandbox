# --------------------------------------------------------
# Author: James Griffiths
# Date Created: Monday, 1st July 2019
# Version: 1.0
# --------------------------------------------------------

# Challenge six ------------------------------------------

# Description: http://www.pythonchallenge.com/pc/def/peak.html
# I have absolutely no idea what this means... a quick Google on 'peak hill' returns posts on
# 'peak hell' pronounces like 'pickle'. I quickly left before seeing too much!
# So, investigate what Pickle is in Python...
# I found this post pretty good:
# https://www.geeksforgeeks.org/understanding-python-pickling-example/
# There is a source file embedded within the page source:
# http://www.pythonchallenge.com/pc/def/banner.p
# So I'll use this to lay some pickle magic down...

from urllib.request import urlopen
import pickle

h = urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(h)

for line in data:
    print("".join([k * v for k, v in line]))

# I had to look up how to display the key and values as a visual representation
# The dictionary key suggests what will be displayed, the value is how many spaces to move...
