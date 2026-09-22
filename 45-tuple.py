thistuple = ("apple", "banana", "cherry")
print(thistuple)


# A tuple is a collection which is ordered and unchangeable

# Tuples can also be created without the parentheses:

thistuple = "apple", "banana", "cherry"
print(thistuple)


# Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Print the number of items in the tuple:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


# One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Create an empty tuple:

thistuple = ()
print(type(thistuple))

# String, int and boolean data types:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# A tuple with strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

thistuple = tuple(["apple", "banana", "cherry"]) # note the double round-brackets
print(thistuple)




