#Importing libraries
from scipy.stats import expon
from scipy.stats import gamma

#Declaring counter and sample_size 
count=0
sample_size=100000

#Declaring the sample space of exp and gamma distribution
X=expon.rvs(size=sample_size,scale=1)
Y=gamma.rvs(a=2,size=sample_size,scale=1)

#Calculating the probability 
for i in range (sample_size):
 if X[i]<Y[i]:
   count+=1

#Printing the stimulated solution   
print("Experimental probability = ", count / sample_size)
print("which is approximately equal to 0.75(theoritical probability)")