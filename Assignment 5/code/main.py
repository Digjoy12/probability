#Importing libraries
import random
import matplotlib.pyplot as plt
import numpy as np

#Declaring a sample size
sample_size=100000

#Declaring the sample space of x and y
x=[0]*sample_size
y=[0]*sample_size
for i in range(sample_size):
    y[i]=random.random()
    x[i]=(1-y[i]**2)**0.5*random.random()
    x[i]=x[i]*np.random.choice([-1,1],p=[0.5,0.5])
    y[i]=y[i]*np.random.choice([-1,1],p=[0.5,0.5])

#Declaring counters    
e_y=0
countX=0
e_xy=0
e_x=0

#Calculating the expectation values and P(X>0)
for i in range(sample_size):
    e_y+=y[i]
    e_xy+=(x[i]*y[i])
    e_x+=x[i]
    if x[i]>0:
        countX+=1
e_y/=sample_size
e_xy/=sample_size
e_x/=sample_size
countX/=sample_size

#Calculating cov(X,Y)
cov=e_xy-(e_y*e_x)

#Printing the results
print("P(X>0)=",countX)
print("which is approximate equal to the theortical value 0.5")

print("E[Y]=",e_y)
print("which is approximate equal to the theortical value 0")

print("Cov(X,Y)=",cov)
print("which is approximate equal to the theortical value 0")

plt.scatter(x,y)
plt.show()
