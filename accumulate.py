import itertools
import operator
numbers=[1,2,3,4,5,6,7,8,9,]
x=itertools.accumulate(numbers,operator.add)
for i in x:
    print (i)