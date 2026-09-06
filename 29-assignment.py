text_1 = "python programming"


# 1.print each character of text_1 on a separate line

for i in text_1:
    print(i)

print("----------------")

# 2. count the total number of characters in text 1

print(len(text_1) )

print("----------------")

# 3. count hiw many times the letter o appears


count_of_o = text_1.count("o")
print(count_of_o)




count_of_o = 0
for i in text_1:
    if i == "o":
        count_of_o = count_of_o + 1

print("count of o in text is   ", count_of_o)
# count_of_i = text_1.count("i")
# print((count_of_i))


print("----------------")

# 4. print only the vowels from text_1:

for i in text_1:
    if i in "aeiou":
        print(i)

print("----------------")

# 5. print only the consonants from text_1:

for i in text_1:
    if i in "bcdfghjklmnpqrstvwxyz":
        print(i)

print("======================================")

## string 2

text_2 = ("Hello World")

# 1. print each character using a for loop:

for i in text_2:
    print(i)

print("----------------------")

# 2. count the number of spaces:

count_number_of_spaces = 0
for i in text_2:
    if i in " ":
        count_number_of_spaces = count_number_of_spaces + 1
print(count_number_of_spaces)

print("-----------------")

# 3. count the number l characters:

count_number_of_l = 0
for i in text_2:
    if i in "l":
        count_number_of_l = count_number_of_l + 1
print(count_number_of_l)

print("-----------------")

# 4. print all uppercase character:

for i in text_2:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXZ":
        print(i)

print("-----------------")

# 5. print all lowercase characters:

for i in text_2:
    if i in "abcdefghijklmnopqrstuvwxyz":
        print(i)


print("======================================")

##string3

text_3 = "Python123"

# 1. print only letter

for i in text_3:
    if i in "abcdefghijklmnopqrstuvwxyz":
        print(i)


print("----------------------")

# 2. print only the numbers:

for i in text_3:
    if i in "0123456789":
        print(i)

print("-----------------")

# 3. count the total number of digits:

count_number_of_digits = 0
for i in text_3:
    if i in "0123456789":
        count_number_of_digits = count_number_of_digits + 1

print("-----------------")

# 4. count the total number of letter:

count_number_of_letters = 0
for i in text_3:
    if i in "abcdefghijklmnopqrstuvwxyz":
        count_number_of_letters = count_number_of_letters + 1
print(count_number_of_letters)

print("-----------------")

# 5. print each character along with its position:
print(text_3[0])
print(text_3[1])
print(text_3[2])
print(text_3[3])
print(text_3[4])
print(text_3[5])
print(text_3[6])
print(text_3[7])
print(text_3[8])

print("===============================")


##string4

text_4 = "Machine Lerning"

# 1. print each character separately:

for i in text_4:
    print(i)


print("-----------------------")


# 2. count the number of vowels:

count_number_of_digits = 0
for i in text_4:
    if i in "aeiou":
        count_number_of_digits = count_number_of_digits + 1

print(count_number_of_digits)


print("-----------------")


# 3. count the number of consonants:

count_number_of_consonants = 0
for i in text_4:
    if i in "bcdfghjklmnpqrstvwxyz":
        count_number_of_consonants = count_number_of_consonants+ 1

print(count_number_of_consonants)

print("-----------------")

# 4. count the number of spaces:

count_number_of_spaces = 0
for i in text_4:
    if i in " ":
        count_number_of_spaces = count_number_of_spaces + 1

print(count_number_of_spaces)

print("-----------------")

# 5. count how many times letter n appears:

count_letter_n = 0
for i in text_4:
    if i in "n":
        count_letter_n = count_letter_n + 1
print(count_letter_n)


print("==================================")



##string 5

text_5 = "Artificial Intelligence 2026"

# 1. print only the alphabetic characters:

for i in text_5:
    if i in "ABXDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
        print(i)

print("-----------------")

# 2. print only the digits:

for i in text_5:
    if i in "0123456789":
        print(i)


print("-----------------")

# 4. count the number of spaces:

count_number_of_spaces = 0
for i in text_5:
    if i in " ":
        count_number_of_spaces = count_number_of_spaces + 1
print(count_number_of_spaces)

print("------------------")


# 5. count how many times the letter i appears:

count_number_of_i = 0
for i in text_5:
    if i in "i":
        count_number_of_i = count_number_of_i + 1
print(count_number_of_i)

print("-----------------")

# 6. print all uppercase letters:

for i in text_5:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(i)

print("-----------------")

# 7. print all lowercase letter:

for i in text_5:
    if i in "abcdefghijklmnopqrstuvwxyz":
        print(i)


print("===================================")

##chlange questions:

text = 'Python is Easy and Powerful'

# 1. total number of characters:

print(len(text))

print("-----------------")


# 2. total number of vowels:

count_number_of_vowels = 0
for i in text:
    if i in "aeiou":
        count_number_of_vowels = count_number_of_vowels + 1

print(count_number_of_vowels)

print("-----------------")

# 3. total number of consonants:

count_number_of_consonants = 0
for i in text:
 if i in "bcdfghjklmnpqrstvwxyz":
     count_number_of_consonants = count_number_of_consonants + 1

print(count_number_of_consonants)

print("-----------------")

# 4. total number of spaces:

count_number_of_spaces = 0
for i in text:
    if i in " ":
        count_number_of_spaces = count_number_of_spaces + 1

print(count_number_of_spaces)

print("-----------------")

# 5. number of upercase letter:

count_number_of_uppercase_letter = 0
for i in text:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        count_number_of_uppercase_letter = count_number_of_uppercase_letter + 1

print(count_number_of_uppercase_letter)

print("-----------------")

# 6. number of lowercase letter:

count_number_of_lowercase_letters = 0
for i in text:
    if i in "abcdfghijklnopqrstuvwxyz":
        count_number_of_lowercase_letters = count_number_of_lowercase_letters + 1
print(count_number_of_lowercase_letters)

print("-----------------")

# 7. number of times o appears

count_number_of_o = 0
for i in text:
    if i in "o":
        count_number_of_o = count_number_of_o + 1

print(count_number_of_o)

# 8. print the string in reverse order:

print("lufrewoP dna ysaE si nohtyP")










