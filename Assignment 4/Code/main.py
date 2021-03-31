#Importing the libraries
import numpy as np
from scipy.stats import bernoulli

#Declaring the sample size
sample_size=100000

#Probability of getting 1,2, or 3
prob_A=0.5

#Probability that the sum is atleast 6 in first roll
prob_B=0.167

#prob(B|A)
prob_A_B=0.5

#Simulations using Bernoulli r.v.
sample_A= bernoulli.rvs(size= sample_size, p =prob_A)
sample_A_B= bernoulli.rvs(size= sample_size, p = prob_A_B)
sample_B= bernoulli.rvs(size= sample_size, p= prob_B)


#calculating probability:
quant_A= np.nonzero(sample_A==1)
quant_A_B= np.nonzero(sample_A_B==1)  
quant_B=np.nonzero(sample_B==1) 

#finding probability of getting sum total of atleast 6
prob_six=  (np.size(quant_B)/sample_size)+((np.size(quant_A)/sample_size)*(np.size(quant_A_B)/sample_size))
print(prob_six)       
print("which is approximately equal to (theoritical value 0.41)")


