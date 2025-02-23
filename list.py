# list in python
# list is a collection which is ordered and changeable. Allows duplicate members.

fruits = ['apple', 'banana', 'cherry']
numbers = [10, 20, 30, 40]
print(fruits) # print the list
print(fruits[0]) # access the first element
print(fruits[1]) # access the second element
print(fruits[2]) # access the third element
print(fruits[-1]) # access the last element
print(fruits[-2]) # access the second-last element
print(fruits[1:]) # slice the list
print(fruits[:2]) # slice the list
print(len(fruits)) # length of the list
# --------------------------------------------------------

# list operations
fruits = ['apple', 'banana', 'cherry']
fruits[1] = 'orange' # change the second element
print(fruits) # print the list
fruits.append('mango') # add an element to the end
print(fruits) # print the list
fruits.insert(1, 'kiwi') # insert an element at index 1
print(fruits) # print the list
fruits.remove('banana') # remove an element
print(fruits) # print the list
fruits.pop() # remove the last element
print(fruits) # print the list
fruits.clear() # remove all elements
print(fruits) # print the list
# --------------------------------------------------------

numbers[1] = 25 # change the second element
print(numbers) # print the list
# --------------------------------------------------------
numbers.append(50) # add an element to the end
print(numbers) # print the list
# --------------------------------------------------------
numbers.insert(1, 15) # insert an element at index 1
print(numbers) # print the list
# --------------------------------------------------------
numbers.remove(20) # remove an element
print(numbers) # print the list
# --------------------------------------------------------
numbers.pop() # remove the last element
print(numbers) # print the list
# --------------------------------------------------------
numbers.clear() # remove all elements
print(numbers) # print the list
# --------------------------------------------------------  
numbers = [10, 20, 30, 40]
print(numbers.index(20)) # index of the element 
# --------------------------------------------------------
print(numbers.count(20)) # count of the element
# --------------------------------------------------------
numbers.sort() # sort the list
print(numbers) # print the list
# --------------------------------------------------------
numbers.reverse() # reverse the list
print(numbers) # print the list
# --------------------------------------------------------
numbers_copy = numbers.copy() # copy the list
print(numbers_copy) # print the list
# --------------------------------------------------------
numbers_list = list(numbers) # convert the tuple to list
print(numbers_list) # print the list
# --------------------------------------------------------
numbers_tuple = tuple(numbers) # convert the list to tuple  
print(numbers_tuple) # print the tuple
# --------------------------------------------------------
numbers_set = set(numbers) # convert the list to set
print(numbers_set) # print the set
# --------------------------------------------------------
numbers_str = str(numbers) # convert the list to string
print(numbers_str) # print the string
# --------------------------------------------------------
numbers_dict = dict(enumerate(numbers)) # convert the list to dictionary
print(numbers_dict) # print the dictionary
# --------------------------------------------------------
numbers_str = ', '.join(str(number) for number in numbers) # convert the list to string
print(numbers_str) # print the string
# --------------------------------------------------------
numbers_list = numbers[:] # copy the list
print(numbers_list) # print the list
# --------------------------------------------------------

# use the list in operator
fruits = ['apple', 'banana', 'cherry']
print('apple' in fruits) # check if 'apple' is present in fruits
print('orange' in fruits) # check if 'orange' is present in fruits

# use the list not in operator
fruits = ['apple', 'banana', 'cherry']
print('apple' not in fruits) # check if 'apple' is not present in fruits
print('orange' not in fruits) # check if 'orange' is not present in fruits

# use the list concatenation
fruits = ['apple', 'banana', 'cherry']
fruits += ['orange', 'mango']
print(fruits) # using += operator

# use the list multiplication
fruits = ['apple', 'banana', 'cherry']  
print(fruits * 2) # using * operator

# use the list append method
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits) # using append() method

# use the list insert method
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, 'orange')  
print(fruits) # using insert() method

# use the list remove method
fruits = ['apple', 'banana', 'cherry']
fruits.remove('banana')
print(fruits) # using remove() method

# use the list pop method
fruits = ['apple', 'banana', 'cherry']
fruits.pop()
print(fruits) # using pop() method

# use the list clear method
fruits = ['apple', 'banana', 'cherry']
fruits.clear()
print(fruits) # using clear() method

# use the list index method
fruits = ['apple', 'banana', 'cherry']
print(fruits.index('banana')) # using index() method

# use the list count method
fruits = ['apple', 'banana', 'cherry']
print(fruits.count('banana')) # using count() method

# use the list sort method
fruits = ['apple', 'banana', 'cherry']
fruits.sort()
print(fruits) # using sort() method

# use the list reverse method
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits) # using reverse() method

# use the list copy method
fruits = ['apple', 'banana', 'cherry']
fruits_copy = fruits.copy() 
print(fruits_copy) # using copy() method

# use the list list method
fruits = ('apple', 'banana', 'cherry')
fruits_list = list(fruits)
print(fruits_list) # using list() method    

# use the list list method
fruits = ['apple', 'banana', 'cherry']
fruits_tuple = tuple(fruits)
print(fruits_tuple) # using tuple() method

# use the list list method
fruits = ['apple', 'banana', 'cherry']
fruits_set = set(fruits)
print(fruits_set) # using set() method

# use the list list method
fruits = ['apple', 'banana', 'cherry']  
fruits_str = str(fruits)
print(fruits_str) # using str() method

# use the list list method
fruits = ['apple', 'banana', 'cherry']
fruits_dict = dict(enumerate(fruits))
print(fruits_dict) # using dict() method

# use the list list method
fruits = ['apple', 'banana', 'cherry']
fruits_str = ', '.join(fruits)
print(fruits_str) # using join() method

# use the list list method
fruits = ['apple', 'banana', 'cherry']
fruits_list = fruits[:]
print(fruits_list) # using slicing

# use the list list method
fruits = ['apple', 'banana', 'cherry']
fruits_list = list(fruits)
print(fruits_list) # using list() method
# --------------------------------------------------------


