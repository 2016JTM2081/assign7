###### this is the first .py file ###########

#!/bin/python

import sys
import collections
print sys.argv[1:]    #print the command line string
dict = {}
for letter in sys.argv[1:]:
	if letter not in dict.keys():
  		dict[letter] = 1
 	else:
  		dict[letter] += 1

print dict           #print the frequency of words

def top3words(dict):
	counts = collections.Counter(dict)
	return [elem for elem, _ in counts.most_common(3)]

x = top3words(dict)
print x           #print the top 3 frequency words

