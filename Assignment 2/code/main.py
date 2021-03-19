import numpy as np
from scipy.stats import bernoulli

#Given set
arr_A=[2,3,4,5]
arr_B=[11,12,13,14,15]

#Declaring a counter
count_p=0

#Declaring a stimulated array of set B
sti_arr_B=np.zeros(shape=5,dtype=int)

print("Stimulation of array B:")
#Stimulating the probabilty
for i in range(0,5):
  index=0
  count=0
  while count!=1:
    count=0
    sti_arr_B=bernoulli.rvs(size=5,p=0.2)
    for j in range(0,5):
      if(sti_arr_B[j]==1):
        count+=1
#Printing the stimulated array      
  print(sti_arr_B)
  for k in range(0,5):
   if(sti_arr_B[k]==1):
      index=k
#Checking the condition
  for q in range(0,4):    
   if(arr_A[q]+arr_B[index]==16):
     count_p+=1

#printing the stimulated probability
print("Stimulated probabilty is:",count_p/20)
print("which is approximately equal to the theortical result")