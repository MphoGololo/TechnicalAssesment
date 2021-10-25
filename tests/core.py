'''
Python 3 program to find sum of digits in factorial of a number

Two functions are used for this functionality. 
	1. Function to multiply x with large number stored in vector. Result is stored in vector.
	2. findSumOfDigits takes the input and returns sum of digits in n!

'''
import numpy as np

def multiply(vector, x):
	carry = 0
	size = len(vector)
	for i in range(size):
		
		# Calculate result + prev carry
		result = carry + vector[i] * x

		# updation at ith position
		vector[i] = result % 10
		carry = result // 10

	while (carry != 0):
		vector.append(carry % 10)
		carry //= 10

# Returns sum of digits in n!
def findSumOfDigits( n):
	vector = []	 # create a vector of type int
	vector.append(1) # adds 1 to the end

	# One by one multiply i to current
	# vector and update the vector.
	for i in range(1, n + 1):
		multiply(vector, i)

	# Find sum of digits in vector vector[]
	sum = 0
	size = len(vector)
	for i in range(size):
		array = i*np.ones((size))
    		vector.append(array)
		sum += vector[i]
	return sum

if __name__ == "__main__":

	n = 1000
	print(findSumOfDigits(n))

