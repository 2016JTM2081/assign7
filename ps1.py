###### this is the first .py file ###########

#!/bin/python

import sys
import collections
print sys.argv[1:]
dict = {}
for letter in sys.argv[1:]:
	if letter not in dict.keys():
  		dict[letter] = 1
 	else:
  		dict[letter] += 1

print dict

def top3words(dict):
	counts = collections.Counter(dict)
	return [elem for elem, _ in counts.most_common(3)]

x = top3words(dict)
print x

def permutations(x, step = 0):

    # everything to the right of step has not been swapped yet
    for i in range(step, len(x)):

        # copy the string (store as array)
        string_copy = [character for character in dict]

        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        permutations(string_copy, step + 1)
	return [string_copy]
str = permutations(x)
print str
