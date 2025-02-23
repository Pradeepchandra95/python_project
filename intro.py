# Run the python script through command line
# python intro.py
# python -c "print('Hello, World!')" - run the python statement script through command line
# python -m module_name - run the module through command line
# python -m pip install package_name - run the package through command line (install the package)
# python -m pip uninstall package_name - run the package through command line (uninstall the package)
# python -m pip list - run the package through command line (list the package)
# python -m pip show package_name - run the package through command line (show the package)
# python -m pip search package_name - run the package through command line (search the package)
# python -m pip freeze - run the package through command line (freeze the package)
# python -m pip check - run the package through command line (check the package)
# python -m pip help - run the package through command line (help the package)
# python -m pip help install - run the package through command line (help the package install)
# python -m pip help uninstall - run the package through command line (help the package uninstall)
# python -m pip help list - run the package through command line (help the package list)
# python -m pip help show - run the package through command line (help the package show)
# python -m pip help search - run the package through command line (help the package search)
# python -m pip help freeze - run the package through command line (help the package freeze)
# python -m pip help check - run the package through command line (help the package check)
# python -m pip help help - run the package through command line (help the package help)
# python -m pip help command - run the package through command line (help the package command)
# python -m pip help options - run the package through command line (help the package options)
# python -m pip help global-options - run the package through command line (help the package global-options)
# python -m pip help subcommands - run the package through command line (help the package subcommands)
# python -m pip help <command> - run the package through command line (help the package <command>)

# --------------------------------------------------------
#  It will print the python directory path
import sys
print('my data', sys.argv)
print('my data 1', sys.argv[0])
# --------------------------------------------------------
# Run the script with arguments through command line
# python script.py arg1 arg2 arg3
# --------------------------------------------------------
# its give the use of different language (no need in python 3 but in python 2 we need to add the encoding-if not use giv the syntax error)
# -*- coding: utf-8 -*-
print("नमस्ते दुनिया!")  # हिंदी में टेक्स्ट
# --------------------------------------------------------
# use for the comment
"""
This is a multiline
comment
""" 
# --------------------------------------------------------
print('Python rocks!') # single quote
print("Python rocks!") # double quote
print('''Python rocks!''') # triple quote
print("""Python rocks!""") # triple double quote
# --------------------------------------------------------
# use the escape character
print('Python rocks!\n') # newline
print('Python rocks!\t pc') # tab
print('Python rocks!\\') # backslash
print('Python rocks!\"') # double quote
print('Python rocks!\'') # single quote
# --------------------------------------------------------
print(r"C:\some\name") # raw string - use to tell python that string is raw string
# --------------------------------------------------------
# use the string concatenation
print('Python' + 'rocks!') # using + operator
print('Python' 'rocks!') # using space
# --------------------------------------------------------
# use the string multiplication
print('Python' * 3) # using * operator
# --------------------------------------------------------
# use the string indexing
word = 'Python'
print(word[0]) # character in position 0
print(word[5]) # character in position 5
print(word[-1]) # last character
print(word[-2]) # second-last character
# --------------------------------------------------------
# use the string slicing
word = 'Python'
print(word[0:2]) # characters from position 0 (included) to 2 (excluded)
print(word[:2]) # character from the beginning to position 2 (excluded)
print(word[2:]) # characters from position 2 (included) to the end
print(word[-2:]) # characters from the second-last (included) to the end
# --------------------------------------------------------
# use the string length
word = 'Python'
print(len(word)) # length of the string
# --------------------------------------------------------
# use the string in operator
word = 'Python'
print('P' in word) # check if 'P' is present in word
print('p' in word) # check if 'p' is present in word
# --------------------------------------------------------
# use the string not in operator
word = 'Python'
print('P' not in word) # check if 'P' is not present in word
print('p' not in word) # check if 'p' is not present in word
# --------------------------------------------------------
# use the string formatting
name = 'Alice'
age = 10
print('My name is {} and I am {} years old.'.format(name, age)) # using format() method
print(f'My name is {name} and I am {age} years old.') # using f-string
print('My name is %s and I am %d years old.' % (name, age)) # using % operator
print('My name is {0} and I am {1} years old.'.format(name, age)) # using format() method
print('My name is', name, 'and I am', age, 'years old.') # using comma
print('My name is ' + name + ' and I am ' + str(age) + ' years old.') # using + operator
# --------------------------------------------------------
# use the string methods
word = 'Python'
print('upper------', word.upper()) # convert the string to uppercase
print('lower------', word.lower()) # convert the string to lowercase
print('capitalize------', word.capitalize()) # convert the first character to uppercase
print('title------', word.title()) # convert the first character of each word to uppercase
print('swapcase------', word.swapcase()) # convert uppercase to lowercase and vice versa
print('startswith------', word.startswith('P')) # check if the string starts with 'P'
print('endswith------', word.endswith('n')) # check if the string ends with 'n'
print('find------', word.find('t')) # find the first occurrence of 't'
print('rfind------', word.rfind('t')) # find the last occurrence of 't'
print('count------', word.count('t')) # count the number of occurrences of 't'
print('replace------', word.replace('t', 'T')) # replace 't' with 'T'
print('strip------', word.strip()) # remove leading and trailing whitespaces
print('lstrip------', word.lstrip()) # remove leading whitespaces
print('rstrip------', word.rstrip()) # remove trailing whitespaces
print('isalnum------', word.isalnum()) # check if all characters are alphanumeric
print('isalpha------', word.isalpha()) # check if all characters are alphabetic
print('isdigit------', word.isdigit()) # check if all characters are digits
print('islower------', word.islower()) # check if all characters are lowercase
print('isupper------', word.isupper()) # check if all characters are uppercase
print('istitle------', word.istitle()) # check if the first character of each word is uppercase
print('isspace------', word.isspace()) # check if all characters are whitespace
print('join------', word.join(['a', 'b', 'c'])) # join the elements of the list with the string
print('split------', word.split('t')) # split the string into a list
print('splitlines------', word.splitlines()) # split the string into a list of lines
# --------------------------------------------------------
word = "Python"
print(word[0])
print(word[-1])
print(word[2:])
print(word[:3])
print(word[1:4])
print(word[-3:])
print(word[-3:-1])
print(word[1:5:2])
print(word[::-1])
# --------------------------------------------------------