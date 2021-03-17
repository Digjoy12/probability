#Given set
A=[2,3,4,5]
B=[11,12,13,14,15]

#Declaring two counters
count=0
fav=0

#Calculating the sample space
print("The sample space is:")
for i in range(0,4):
 for j in range(0,5):
   print((A[i],B[j]), end=" ")
   count+=1

#Printing the size of sample space
print("\n")  
print("The total numbers of elements in sample space is:",count)

#Calculating the favourable events
print("\nThe favourable elements are:")
for i in range(0,4):
  for j in range(0,5):
    if(A[i]+B[j]==16):
     print((A[i],B[j]), end=" ")
     fav+=1 

#Printing the size of favourable events
print("\n")  
print("The total numbers of favourable elements is:",fav)   

#Calculating the Probabilty
print("\nProbabilty of that the sum of the two numbers equals 16 is:",fav/count)
print("is equal to the theortical value=0.2")