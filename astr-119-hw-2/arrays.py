x = [0.0, 3.0, 5.0, 2.5, 3.7]
print(type(x))

print("originally, x = ", x)
#remove the third element
x.pop(2)
print(x)

#remove the element equal to 2.5
x.remove(2.5)
print(x)

#get a copy of x
y = x.copy()
print(y)

#how many elements equal to zero
print(y.count(0.0))

#prints the index with val 3.7
print(y.index(3.7))

#sort the list
print("i'm gonna insert 7.9 at the beginning of array y")
y.insert(0, 7.9)
print("unsorted: ", y)
y.sort()
print("sorted: ", y)

#reverse sort
y.reverse()
print(y)

#remove all elements
y.clear()
print(y)