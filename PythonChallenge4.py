# --------------------------------------------------------
# Author: James Griffiths
# Date Created: Monday, 1st July 2019
# Version: 1.0
# --------------------------------------------------------

# Challenge five -----------------------------------------

# Description: http://www.pythonchallenge.com/pc/def/linkedlist.html
# All the page displays is:
# linkedlist.php
# going to http://www.pythonchallenge.com/pc/def/linkedlist.php gives me a picture and
# in the source code I'm told:
# "urllib may help. DON'T TRY ALL NOTHINGS, since it will never end. 400 times is more than enough."
# the picture has a URR variable of:
# nothing=12345
# clicking on the image I get the message
# "and the next nothing is 44827"
# So, I replaced the URL variable with the 'next nothing' value of 44827 and got:
# "and the next nothing is 45439"
# Ok, so if I just loop this action 400 times I should get my value for the next challenge..?

# The first URL: http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
import urllib.request
import re


def n(newVariable):
    counter = 1
    newV = newVariable
    while counter < 400:

        if newV == str(16044):
            newV = int(newV) // 2

        html = urllib.request.urlopen(
                    "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(newV)).read().decode()

        newV = re.findall("next nothing is (.*)", html, re.DOTALL)[-1]

        print(str(counter) + " variable is: " + str(newV))

        counter = counter + 1

    return newV


newPage = n(input("What is the starting variable? "))
print("The solution page is: " + str(newPage) + ".html")

# The above 'works' but I get a 'list index out of range' at loop 84
# I manually added the 84th value and got a string:
# "Yes. Divide by two and keep going.: Grr...
# Ok, I need to add in a catch - see line 32 and 33
# Stops again on the 140th call:
# There maybe misleading numbers in the text. One example is 82683. Look only for the next
# nothing and the next nothing is 63579
# I need to edit the findall to look for 'next nothing is ' instead of 'is '
# Call 250 returns: 'peak.html' I'm assuming this is the solution...
# Messy code, but works. Needs a revisit!
