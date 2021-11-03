#!/usr/bin/env python3

from integer import Integer
import random
import matplotlib.pyplot as plt
import time

def fib_py(n):
    if n<=1:
        return n
    else:
        return (fib_py(n-1) + fib_py(n-2))


def matrix(n): #n number of random points
    c=0
    x=[]
    y=[]
    while c<n:
        #creating random x and y
        x.append(random.uniform(-1, 1))
        y.append(random.uniform(-1, 1))
        c+=1
    return list(zip(x,y))

def incircle(x,y):
    xi=0
    yi=0
    r=1
    return ((x-xi)**2+(y-yi)**2)<=r**2 #output of the function is True or Flase

def counting(n):
    z=matrix(n)
    count=0
    for i in z:
        x=i[0]
        y=i[1]
        count+=incircle(x,y)
    return 'We found {} number of points out of {} random tries for a {} accuracy, resulting in a pi approximation of {}.'.format(count, n, count/n, 4*count/n)
    
def main():
    
    
	#C++ timings
    nc = []
    tc = []
    for n in range(30,45):
        f= Integer(n)
        tstart = time.perf_counter ()
        f.fib()
        tstop = time.perf_counter ()
        ttaken = tstop - tstart
        tc.append(ttaken)
        nc.append(n)
    print(tc)
	# Python timings
    np = []
    tp = []
    for n in range(30,45):
        tstart = time.perf_counter ()
        fib_py(n)
        tstop = time.perf_counter ()
        ttaken = tstop - tstart
        np.append(n)    
        tp.append(ttaken)
    print(tp)
    plt.plot(nc,tc)
    plt.plot(np,tp)
    plt.savefig("FibonacciTime.png")
    
    # f = Integer(5)
    # print(f.get())
    # f.set(7)
    # print(f.get())

if __name__ == '__main__':
    main()