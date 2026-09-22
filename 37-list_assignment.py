

fruits = ["apple", "banana", "cherry", "mango", "orange"]

# Write Python code to:
#
# Print the first item.
# Print the third item.
# Print the last item using negative indexing.
# Print the second-last item.

print(fruits[0])
print("------------------")
print(fruits[2])
print("------------------")
print(fruits[-1])
print("------------------")
print(fruits[3])
print("===========================")

# Question 2

# Given:

colors = ["red", "green", "blue", "yellow", "black", "white"]

# Print:
#
# "green"
# "yellow"
# "white"
# The first three items using slicing.
# Items from index 2 to index 5.
print(colors[1])
print("--------------------")
print(colors[3])
print("--------------------")
print(colors[-1])
print("--------------------")
print(colors[0:2])
print("--------------------")
print(colors[2:5])
print("=============================")

# Given:

students = ["Ali", "Ahmed", "Sara", "Usman", "Ayesha"]

# Use negative indexing to print:
#
# The last student.
# The second-last student.
# The third-last student.
# Part 2 — Check if an Item Exists

print(students[-1])
print("----------------------")
print(students[-2])
print("----------------------")
print(students[-3])
print("----------------------")
# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")
if "Ahmed" in students:
    print("yes,'Ahmed' in students")

print("===========================")


# Question 4
#

# Create a list:
#
languages = ["Python", "Java", "C++", "JavaScript"]

# Use the in operator to check:
#
# Is "Python" present?
# Is "PHP" present?

# Print the results.

# Expected output:
#
# True
# False
# Part 3 — Change List Items


print("Python" in languages)
print("---------------------")
print("PHP" in languages)
print("----------------------")
languages[1]="CSS"
print(languages)
print("==============================")

# Question 5
#
# Given:

fruits = ["apple", "banana", "cherry"]

# Change "banana" to "mango".
#
# Expected result:
#
# ["apple", "mango", "cherry"]

fruits[1]="mango"
print(fruits)
print("==============================")

# Question 6
#
# Given:

cars = ["Toyota", "Honda", "BMW", "Audi"]

# Change:
#
# "Honda" → "Suzuki"
# "BMW" → "Mercedes"
#
# Print the final list.
#
# Part 4 — Change Multiple List Items
cars[1:3]=["Suzuki","Mercedes"]
print(cars)
print('-------------------------------')
# cars[2]="Mercedes"
# print(cars)


# Question 7
#
# Given:
#
numbers = [10, 20, 30, 40, 50]

# Change the second and third items to:
#
# 200
# 300
#
# Expected output:
#
# [10, 200, 300, 40, 50]

numbers[1:3] = ["200","300"]
print(numbers)
print("============================")

# Question 8
#
# Given:

animals = ["cat", "dog", "lion", "tiger", "horse"]

# Using slicing, replace "lion" and "tiger" with:
#
# "elephant", "zebra"
#
# Expected output:
#
# ["cat", "dog", "elephant", "zebra", "horse"]

animals[2:4]=['elephant','zebra']
print(animals)
print("==========================")

# Question 9
#
# Create a list containing 5 student names.
#
# Write a program that:
#
# Prints the first student.
# Prints the last student.
# Changes the third student's name.
# Prints the updated list.

Students = ["ali",'ismail','farhan','sheri','basit']

print(Students[0])
print("-------------------------")
print(Students[-1])
print("-------------------------")
Students[2]='mubashir'
print(Students)
print("=============================")

# Question 10 — Mini Project
#
# Create a shopping list program:

shopping = ["Milk", "Bread", "Eggs", "Rice", "Sugar"]

# Your program should:
#
# Print the first item.
# Print the last item.
# Check whether "Rice" exists.
# Change "Sugar" to "Tea".
# Change "Bread" to "Biscuits".
# Print the final shopping list.
print(shopping[0])
print('---------------------')
print(shopping[-1])
print('---------------------')
if "Rice" in shopping:
    print("Rice is in the shopping")
print('---------------------')
shopping[-1]='Tea'
print(shopping)
print('---------------------')
shopping[1]='Biscuits'
print(shopping)
