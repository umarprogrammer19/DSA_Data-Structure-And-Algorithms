# Check if a string is a palindrome.
string = input("Enter a string to check a palindrome: ")
if string == string[::-1]:
    print(string, "is Palindrome")
else:
    print(string, "is not Palindrome")

# Count vowels and consonants in a string.
s = input("Enter a string to count the vowels and consonants: ")
vowels = ["a", "e", "i", "o", "u"]
vov, cons = 0, 0

for val in s:
    if val.lower() in vowels:
        vov += 1
    elif val.isalpha():
        cons += 1

print("Vowels:", vov)
print("Consonants:", cons)

# Find the frequency of each character in a string.
s = input("Enter a string to find the frequency in it: ")
freq = {}

# Simple Method
for c in s:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1
print(freq)

# With Counter
from collections import Counter

freq = Counter(s)
print(dict(freq))

# Dictionary Comprehension
freq = {c: s.count(c) for c in s}
print(freq)

# Reverse a string without using built-in functions.
s = input("Enter a string to reverse string: ")
rev = ""
for c in s:
    rev = c + rev
print(rev)

# Capitalize the first letter of each word in a string.
s = input("Enter a string to Capitalize 1st car in string: ")
print(" ".join([c.capitalize() for c in s.split()]))

