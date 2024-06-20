#ordinal value comparison
print(ord('a'))
print('aa'>'ab')

#set 
s={55,9,9,2,5}
s1={1,2,4,5,6,4,9}
s.add('a')
s.remove(5)
s.union(s1)
print(s.intersection(s1))
print(s)
print(55 in s) #happens much much faster than in lists

#dict 
d={}
d["k1"]=5
for k,v in d.items():
    print(k,v)
del d['k1']

#use comprehensions with anything 
dic={"k"+str(i) : i for i in range(100) if i%5==0}

# *args and **kwargs AWESOME
def awo(arg1,*args): #pass variable number of arguments
    print(args)
    print(type(args)) # args is a tuple
    print(args[2])

awo(1,23,4,"abhay")

print('now testing kwargs')
#keyword arguements, like a dict
def awok(**kwargs):
    print(kwargs)
    print(type(kwargs))
    # print(kwargs[0])
    print(kwargs['first'])
    for i,j in kwargs.items():
        print(i,j)

awok(first=1,mid='hello',last=True,test=1.3)


#unpacks the elements of the list and can also be used to unpack to functions
x=[1,2,3,5]
print(x)
print(*x)

def mul(a,b,c,d):
    print(a*b*c*d)
def mul1(*args):
    ans=1
    for i in args:
        ans*=i
    print(ans)

mul(*x)
print('now the alternate way')
mul1(12,4,23,54,2345,23)

#good use of kwargs and args
class Boy():
    def __init__(self,*args,**kwargs):
        self.age=kwargs['a']
        self.height=kwargs['h']
        self.bills=list(args)
    
abhay= Boy(100,200,250,h=177,a=19)

print(abhay.height)


#lambda: one line anonymous function
f= lambda p,q : p*q
print(f(2,5))

#map and filter 
q=[23,5,45,2,53,2345,2,342,134,3]

mp= map(lambda i:i*3, q) #list ke har element par operation karke new list mai mapped
print(list(mp))

fil= filter(lambda k: k<=5,q)
print(list(fil))
print("here") 


#format
a=2
b=3
print("a is {} and b is {}".format(a,b))

#numpy
# import numpy as np
