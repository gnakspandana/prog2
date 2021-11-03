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
    # n=50
    # z= matrix(n)
    # z_x=z[0][0]
    # z_y=z[0][1]
    # print(z)
    # print("x,y",z_x,z_y)
    # incircle(z_x,z_y)
    # print(counting(n))
    # print(incircle(1,1))
    # plt.figure(figsize=(9,9))
    # # theta= linspace(0,2*np.pi,100)
    # # x=1+1*cos(theta)
    # # y=1+1*sin(theta)
    # L=[50,500,1000,5000]
    # for i in L:
    #     x1,y1=[],[]
    #     x2,y2=[],[]
    #     z=matrix(i)
    #     for j in range(0, len(z)):
    #         if (incircle(z[j][0],z[j][1])):
    #             x1.append(z[j][0])
    #             y1.append(z[j][1])
    #         else:
    #             x2.append(z[j][0])
    #             y2.append(z[j][1])
    #     plt.subplot(2,2,(L.index(i)+1))
    #     #plt.plot(x,y,clor='red')
    #     plt.scatter(x1,y1, color='red')
    #     plt.scatter(x2,y2, color='blue')
    #     plt.plot()
    
    
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
    # f = Integer(5)
    # print(f.get())
    # f.set(7)
    # print(f.get())

if __name__ == '__main__':
    main()