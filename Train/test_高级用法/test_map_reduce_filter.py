print(list(map(lambda x:x*x,[1,2,3,4,5])))


# --------------------------------------- map 入参(function, itable)
from functools import  *

print(reduce(lambda x,y:x+y, [1,2,3,4,5]))


# --------------------------------------- reduce 入参(function 两个入参 , itable)


print(list(filter(lambda x:x % 2 ==0,[2,3,4,5,6])))

