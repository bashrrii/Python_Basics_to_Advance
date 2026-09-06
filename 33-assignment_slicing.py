a = "http/www.google.com/learing/python/opencv"

# slice on the basis of /

print(a[4:20])




# Task 1: Employee Registration System (10 Marks)
#
# A company stores employee names entered by HR.
#
# Sample Input
# employee = "   muhammad ali khan   "
# Requirements
#
# Use the following methods:
#
# strip()
# title()
# upper()
# lower()
# capitalize()
# Expected Output
# Original:
# "   muhammad ali khan   "
#
# After strip:
# muhammad ali khan
#
# Title:
# Muhammad Ali Khan
#
# Upper:
# MUHAMMAD ALI KHAN
#
# Lower:
# muhammad ali khan
#
# Capitalize:
# Muhammad ali khan



###1...

employee = "   muhammad ali khan   "
print(employee.strip())

print("--------------------------")

###2...

print(employee.title())

print("---------------------------")


###3...

print(employee.upper())

print('-----------------------------')

###4...

print(employee.lower())

print("---------------------------")

###4...

print(employee.capitalize())


print("=======================================")



#  Task 2: Email Validation System (10 Marks)
#
# Given
#
# email = "student123@gmail.com"
#
# Check
#
# startswith()
# endswith()
# find("@")
# count("@")
# replace()
#
# Requirements
#
# Replace gmail.com with company.com
# Validate email format


email = "student123@gmail.com"


print(email.startswith("student123"))

print("--------------------------")

print(email.endswith("@gmail.com"))

print("---------------------------")


print(email.find("@"))

print("----------------------------")

print(email.count("@"))

print("------------------------------")

print(email.replace("gmail.com","company.com"))


# Task 3: Product Code Analyzer (10 Marks)
#
# Given
#
# product = "LAPTOP-HP-2025"
#
# Use
#
# split()
# partition()
# rpartition()
# join()
#
# Output
#
# Brand
# Category
# Year
#
# Then create
#
# HP|LAPTOP|2025
#
# using join().




product = "LAPTOP-HP-2025"

brand = "HP"
category = "LAPTOP"
year = "2025"

# print(product.split("-"))
print(brand.split())
print(category.split())
print(year.split())

print("------------------------------")


print(product.partition("-"))


print("---------------------------------")

print(product.rpartition("-"))










print("=========================================")

#
# task4 : user login validator

username = "student_01"
password = "Pass12345"

print(username.isidentifier())
print(username.isalnum())
print(username.isalpha())
print(username.isdigit())
print(username.isnumeric())

print("-----------------------")

print(password.isidentifier())
print(password.isalnum())
print(password.isalpha())
print(password.isdigit())
print(password.isspace())

print("-----------------------")

task5 = "   Total Sales = 250000 PKR   "

# use

print(task5.strip())

print("---------------------")

print(task5.replace("PKR","RS"))

print("-----------------------")

print(task5.split(" "))
print("-----------------------")


sales = '250000'
print(sales)
print("-----------------------")

sales = int(250000)
print(type(sales))

print("============================")

count = 0
password = "Python@123"
for i in password:
    if i.isdigit():
        count = count + 1

print(count)
print("---------------------------")
password = "Python@123"
symbol = 0
digit = 0
alpha = 0

for i in password:
    if i.isdigit():
        digit = digit + 1
    if i.isalpha():
            alpha = alpha + 1
# print(digit)
# print(alpha)
symbol = len(password)-digit-alpha
print(symbol)

print("--------------------------")

# Task 7: Chat Application Formatter (10 Marks)
#
# Input
#
# message = "hello everyone welcome to python programming"
#
# Use
#
# title()
# capitalize()
# center()
# ljust()
# rjust()
#
# Display the message in different alignments.
#
message = "hello everyone welcome to python programming"

print(message.title())

print("---------------------------------")

print(message.capitalize())

print("---------------------------------")

print(message.center(100))

print("----------------------------------")

print(message.rjust(50))

print("-----------------------------------")

print(message.ljust(50))

print("====================================")

# Task 8: Log File Processing (10 Marks)
#
# Given
#
# log = "INFO:Server Started Successfully"
#
# Use
#
# partition(":")
# split(":")
# find()
# index()
#
# Extract
#
# INFO
# Server Started Successfully

log = ("INFO:Server Started Successfully")


print(log.partition(":"))

print("-------------------")


print(log.split(":"))

print("---------------------------")

print(log.find(":"))

print("--------------------------")

print(log.index(":"))

print("---------------------------")

print(log[:4])
print("--------------------------")

print(log[5:])

print("==================================")

# Task 9: Customer Feedback Analyzer (10 Marks)
#
# Input
#
# feedback = "Good product. Good quality. Good packaging."
#
# Use
#
# count()
# replace()
# split()
#
# Find
#
# Number of "Good"
# Replace Good with Excellent
# Total words

feedback = "Good product. Good quality. Good packaging."

print(feedback.count("Good"))

print("-----------------------------")

print(feedback.replace("Good","Excellent"))

print("------------------------------")

x = feedback.split(" ")
print(x)





print("================================")

# Task 10: Invoice Generator (10 Marks)
#
# Given
#
# name="Ali"
# product="Laptop"
# price=85000
#
# Use
#
# format()
# format_map()
#
# Generate
#
# Customer : Ali
# Product  : Laptop
# Price    : 85000

name="Ali"
product="Laptop"
price=85000



# string.format(value1, value2...)
txt = "name  =  {name}"
txt2 = "product  =  {prod}"
txt3 = "price  =  {price}"

print(txt.format(name = "Ali"))
print(txt2.format(prod = "Laptop"))
print(txt3.format(price = 85000))


