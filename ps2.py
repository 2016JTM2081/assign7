###### this is the second .py file ###########

#!/bin/python
import random
import math
j = 0.0
i = 0.0
for i in list(range(10)):      #iterarte for 10 times
	(X,Y)=(random.random()*2- 1, random.random()*2-1)    #x and y are generated
	c = (X ** 2 + Y ** 2)
	d = math.sqrt( c )
	i += 1
	if d <= 1:
		j += 1
	
print i                  #no. of points in the square
print j                  #no. of points in the circle
percent = (j/i) * 100
print percent
