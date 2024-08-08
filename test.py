import numpy as np
a=np.array([[2,5],[1,6],[3,4],[1,2]])
b=np.array([3,4,5,2])
# print(a*b)

c=0
d=9
e=np.array([c,d])
print(e)

f=np.array([[1,2,3]])
print(f[0][1])

r=[]
for i in range(4):
    i=[1,2,3]
    r.extend(i)

print(r)

a=[i for i in range(16)]
print(a[::-1])
b=[]
size=4
for i in a[::-1]:
    n=4
    r=0
    if i/size==n and i%size==r:
        b.append(a)
    n-=1    
    if n==0:
        r+=1
        n=4
    if r==3:
        break


print(b)