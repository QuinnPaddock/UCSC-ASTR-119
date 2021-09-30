#function definition
def flow_control(k):

	#def a string based on the val of k
	if(k==0):
		s = "variable k = %d equals 0." % k

	elif(k==1):
		s = "variable k = %d equals 1." % k

	else:
		s = "variable k = %d does not equal 0 or 1." % k

	print(s)
#main function definition
def main():
	i = 0

	#try flow control for 0,1,2
	flow_control(i)
	
	i = 1
	flow_control(i)

	i = 2
	flow_control(i)

#main program
if __name__ == "__main__":
	main()