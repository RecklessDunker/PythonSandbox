# --------------------------------------------------------
# Author: James Griffiths
# Date Created: Saturday, 29th June 2019
# Version: 1.0
# --------------------------------------------------------

# Challenge Four -----------------------------------------

# Description: http://www.pythonchallenge.com/pc/def/equality.html

# Hmm, 'One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.'
# The image shows a small candle with three big candles either side of it.
# ...

# Ok, I wanted to get the data in a different way this time, so I looked up how to read a URL
# then extract all the content between the <!-- and --> sections...
import urllib.request
import re

html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()
data = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]

# I then looked for a letter sat between three CAPITAL characters, then joined all the results together...
# I had to look up to get some help with the regex
print("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data)))