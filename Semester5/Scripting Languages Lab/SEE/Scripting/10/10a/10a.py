from functools import reduce
l1 = [2,3,4,2,5,6]
print(l1)
newlist = [i*3 for i in l1]
print(newlist)

sum1 = reduce(lambda x,y : x+y ,l1 )
sum2 = reduce(lambda x,y : x+y ,newlist )

print(sum1,sum2)