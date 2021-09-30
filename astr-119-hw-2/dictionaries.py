#def a dictionary data structure

#dictionaries have key : value for the elements
example_dict = {
	"class" : "Astr 119",
	"prof" : "Brant",
	"Student" : "Quinn",
	"Epic gamer status" : 5
}
print(type(example_dict)) #should say dict

#get a val via key
course = example_dict["class"]
print(course)

#change a val via key
example_dict["Epic gamer status"] += 1 #increase gamer presteige 

#print dictionary
print(example_dict)

#print dict element by element
for x in example_dict.keys():
	print(x, example_dict[x])