# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 22:32:16 2021

@author: koshv
"""

import numpy as np

'''
## Time spent by the star above the horizon
a1 , b1, c1= input('declination (deg min sec), Star : ').split()
a2 , b2, c2= input('latitude (deg min sec), telescope :').split()

a1 = float(a1)
a2 =float(a2)
b1 = float(b1)
b2 = float(b2)
c1= float(c1)
c2 = float(c2)

if a1<0:
    star = -((-a1) + (b1*60 + c1)/3600 )*(np.pi/180)   # radian
else : 
    star = (a1 + (b1*60 + c1 )/3600  )*(np.pi/180)   # radian 

if a2<0:
    tele = -((-a2) + (b2*60 + c2)/3600 )*(np.pi/180) # radian
else:
    tele = (a2 + (b2*60 + c2 )/3600 )*(np.pi/180)  # radian

def func(x,y):
    a = 1 - (np.arccos(np.tan(x)*np.tan(y)) ) /(np.pi) 
    return(a*24)
    
print('time spend by star above horizon',func(star,tele),'hrs')

'''
import matplotlib.pyplot as plt
from scipy.stats import poisson
import math as m
## Undergrads experiment 
# PROBLEM  5

time = [0,1,2,3,4,5,6,7,8,9,10]
freq = [1,9,20,24,19,11,11,0,3,1,1]
a =0
b= 0
# Mean
for i in range(len(time)):
    a=  a+time[i]*freq[i]
    b = b+ freq[i]
mean = a/b
print('Mean',mean)

# Standard deviation
c =0
d =0
for i in range(len(time)):
    c= c+ ((time[i]-mean)**2)*freq[i]

std = np.sqrt(c/b)
print('Std',std)

# histogram and poisson

def poison(x,l):
    n = np.exp(-l)*(l**x/(m.factorial(x)))
    return(n)
    
    
x = np.arange(0,10,1)
y=[]
y1 = []
for i in x:
     y.append(poison(i,3.61))
     y1.append(poison(i,3.7))
fig,ax = plt.subplots()
plt.plot(x,y,label='observed')
plt.plot(x,y1,label = 'parent')

plt.ylabel('poison pdf')
plt.xlabel('x')
freqc = []
for i in freq:
    freqc.append(i/100)
    
ax.step(time,freqc,where='mid',label = 'histogram')
plt.legend()
plt.show()


    
    
    



