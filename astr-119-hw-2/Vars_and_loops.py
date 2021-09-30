import numpy as np #import of numpy

def main():
	i = 0 #i is an integer, declared with a number 0
	n = 10 #n is another integer

	#we can use numpy to declare arrays quickly
	y = np.zeros(n, dtype=float) #if we printed y, it would be a series of zeros

	#we can use for loops to iterate with a variable
	for i in range(n): # i in range [0,n-1]
		y[i] = 2.0 * float(i) + 1.0 #set y = 2*i+1 as floats

	#we can simply iterate through a variable array
	for y_element in y:
		print(y_element)

#execute main function
if __name__=="__main__":
	main()
