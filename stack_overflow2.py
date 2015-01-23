__author__ = 'rsukla'

i = [1, 2, 3, 5, 8, 13]
j = []
k = 0

for l in i:
    print l
    print k
    j[k] = l
    k += 1

print j

'''

j is an empty list, but you're attempting to write to element [0] in the first iteration, which doesn't exist yet.

Try the following instead, to add a new element to the end of the list:

for l in i:
    j.append(l)

'''

'''
use append instead of assignment operator when you are trying to add a new value
'''