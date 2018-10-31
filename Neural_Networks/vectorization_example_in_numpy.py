#vectorization example in numpy
import  numpy as np
a = np.array([1,2,3,4])




import time


print 'Create 2 100,000 element vectors, here are first 10 from each'
a = np.random.rand(1000000)
b = np.random.rand(1000000)
print 'a[0:10] is :', '\n',a[0:10], '\n'*2 
print 'b[0:10] is :', '\n',b[0:10], '\n'*2 
tic = time.time()

c = np.dot(a,b)
print 'c = np.dot(a,b) has type ',type(c), '   because element-wise dot product of 2 arrays'
toc = time.time()
print 'c=  ',c
print ('and the vectorized version took:' + str(1000*(toc-tic)) + ' ms' + '\n'*5) 

print 'Now we consider the loop version'
c=0
tic = time.time()
for j in range(1000000):
    c = c + a[j] * b[j]
toc = time.time()
print 'c=  ',c
print ('The loop version took :' + str(1000*(toc-tic)) +  ' ms')



print '\n'*10, 'some other vectorization examples'
v = np.array([1,2,3,4, 1,2,3,4,5,6])

tic = time.time()
u=np.exp(v)
toc = time.time()
print ('Vectorized version :' + str(1000*(toc-tic)) + 'ms' + '\n'*5)

print u

n=10
u=np.zeros((n,1))
tic = time.time()

for k in range(n):
    u[k] = np.exp(v[k])
toc = time.time()
print ('for loop version :' + str(1000*(toc-tic)) + 'ms' + '\n'*5)
    

np.reshape(u, 10)
print u
