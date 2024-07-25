#set
fruits = set(["red","green","black","red"])
print(fruits)

numbers = set([10,20,3,20,40,1])
print(numbers)

list = {1,2,3,4,3,2}
print(type(list))

list = {1,2,3,4,3,2}
print(type[list])


numbers = [10,20,3,20,40,1,20,3]
print(set(numbers))


list = {}
print(type(list))


list = set()
print(type(list))

#add()
numbers = {1,3,5}
numbers.add(4)
print(numbers)

colours = {"red","blue","green"}
colours.add("white")
print(colours)

#update()

numbers = {10,20,3,20,40,1,20,3}
numbers.update(numbers,{15})
numbers.add(60)
print(numbers)
print(sorted(numbers))

#pop()
list = {10,20,30,40,30,20,50}
print(list)
list.pop()
print(list)

list = {20,30,40,30,False,True}
list1 = {1,30,40,30,False,True}
print(list)

#remove
numbers = {10,20,3,20,40,1,20,3}
numbers.remove(20)
print(numbers)


#discard()
my_set = {1,2,3,4,5} 
my_set.discard(4)
print(my_set)

#clear()

my_set = {1,2,3,4,5}
my_set.clear()
print(my_set)

