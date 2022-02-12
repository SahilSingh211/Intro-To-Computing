from ctypes import Union


s1=[1,2,3,4,5]
s2=[2,4,6,8]
s3=[1,5,9,13,17]
s4=[1,2,3,4,5,6,7,8,9,10]
set1=set(s1)
set2=set(s2)
set3=set(s3)
set4=set(s4)
#part a
a=((set1.union(set2))-(set1.intersection(set2)))
print(a)
b=((set1.union(set2.union(set3)))-(set1.intersection(set2.intersection(set3))))
print(b)

c=((set4)-(set1))
print(c)
d=((set4)-(set1.union(set2).union(set3)))
print(d)
