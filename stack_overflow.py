__author__ = 'rsukla'

l=[1,2,3,0,0,1]
for i in range(0, len(l)):
    print len(l)
    print i
    if l[i]==0:
        l.pop(i)

'''
You are reducing the length of your list l as you iterate over it, so as you approach the end of your indices in the
range statement, some of those indices are no longer valid.

It looks like what you want to do is:

l = [x for x in l if x != 0]

which will return a copy of l without any of the elements that were zero (that operation is called a list comprehension, by the way).
You could even shorten that last part to just if x, since non-zero numbers evaluate to True.

There is no such thing as a loop termination condition of i < len(l), in the way you've written the code,
because len(l) is precalculated before the loop, not re-evaluated on each iteration. You could write it in such a way, however:

i = 0
while i < len(l):
   if l[i] == 0:
       l.pop(i)
   else:
       i += 1
'''
'''
Because of the pop operation you are reducing the length of the indices.
'''
'''
The expression len(l) is evaluated only one time, at the moment the range() builtin is evaluated.
The range object constructed at that time does not change; it can't possibly know anything about the object l.
'''
