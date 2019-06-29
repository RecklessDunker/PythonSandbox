# --------------------------------------------------------
# Author: James Griffiths
# Date Created: Wednesday, 26th June 2019
# Version: 1.0
# --------------------------------------------------------

# Challenge Two ------------------------------------------

# Description: http://www.pythonchallenge.com/pc/def/map.html
# I think the challenge wants me to find and replace the letters in th image
# K = M, O = Q, E = G
# But looking at the pattern, the code suggests moving the letters by two places
# Solving the string offered hints at using string.maketrans() I did not know of this function so
# used a more brute force solution below...

def unscramble(originalText):

    otext = list(originalText)
    ntext = list()
    low = 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'


    for letter in otext:
        if letter in low:
            getCharValue = ord(letter) + 2
            if getCharValue > 122:
                getCharValue = getCharValue - 26
            newletter = chr(getCharValue)
            ntext.append(newletter)
        else:
            ntext.append(letter)

    return ''.join(ntext)



nText = unscramble(input("what is the text you want unscrambling? "))
print(nText)