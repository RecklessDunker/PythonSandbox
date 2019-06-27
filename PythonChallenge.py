# --------------------------------------------------------
# Author: James Griffiths
# Date Created: Wednesday, 26th June 2019
# Version: 1.0
# --------------------------------------------------------


# Challenge One ------------------------------------------
# Description: http://www.pythonchallenge.com/pc/def/0.html
# I think the challenge wants me to work out 2**38...
# Which the below is 274877906944 add the suffix: 274877906944.html

# My solution:
# print(2**38)


# Challenge Two ------------------------------------------

# Description: http://www.pythonchallenge.com/pc/def/map.html
# I think the challenge wants me to find and replace the letters in th image
# K = M, O = Q, E = G
# But looking at the pattern, the code suggests moving the letters by two places

def unscramble(originalText):

    for letter in originalText:
        newletter = ord(letter) + 2
        newtext = originalText.replace(letter, chr(newletter), 1)

    return newtext


newText = unscramble(input("what is the text you want unscrambling? "))
print(newText)


