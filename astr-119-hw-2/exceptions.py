#python exceptions let you deal with unexpected results

try:
	print(a) #this will throw an exception because a is not defined
except:
	print("a be undefined, matey!")

#there are specific errors
try:
	print(a)
except NameError:
	print("Arg, a still be undefined!")
except:
	print("Something else is amiss")

print(a) #this will break the program