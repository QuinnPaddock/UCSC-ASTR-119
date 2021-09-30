#string

s = "This here be a string"
print(type(s))

#Boolean
yes = True
print(type(yes)) ##boolean

no = False
print(type(no))

#list -- ordered and changeable
alpha_list = ["a", "b", "c"] #list initialization
print(type(alpha_list))
print(type(alpha_list[0]))
alpha_list.append("d")
print(alpha_list)

#tuple -- order and unchangable
alpha_tuple = ("a", "b", "c")
print(type(alpha_tuple))

try:
	alpha_tuple[2] = "d"
except TypeError:
	print("Ye can't change elements of a tuple, lad")
print(alpha_tuple)