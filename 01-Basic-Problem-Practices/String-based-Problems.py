# # Check if a string is a palindrome.
# string = input("Enter a string to check a palindrome: ")
# if string == string[::-1]:
#     print(string, "is Palindrome")
# else:
#     print(string, "is not Palindrome")

# # Count vowels and consonants in a string.
# s = input("Enter a string to count the vowels and consonants: ")
# vowels = ["a", "e", "i", "o", "u"]
# vov, cons = 0, 0

# for val in s:
#     if val.lower() in vowels:
#         vov += 1
#     elif val.isalpha():
#         cons += 1

# print("Vowels:", vov)
# print("Consonants:", cons)

# # Find the frequency of each character in a string.
# s = input("Enter a string to find the frequency in it: ")
# freq = {}

# # Simple Method
# for c in s:
#     if c in freq:
#         freq[c] += 1
#     else:
#         freq[c] = 1
# print(freq)

# # With Counter
# from collections import Counter

# freq = Counter(s)
# print(dict(freq))

# # Dictionary Comprehension
# freq = {c: s.count(c) for c in s}
# print(freq)

# # Reverse a string without using built-in functions.
# s = input("Enter a string to reverse string: ")
# rev = ""
# for c in s:
#     rev = c + rev
# print(rev)

# # Capitalize the first letter of each word in a string.
# s = input("Enter a string to Capitalize 1st car in string: ")
# print(" ".join([c.capitalize() for c in s.strip().split()]))
# print(s.title())

# # Count the number of words in a sentence.
# s = input("Enter a string to find a number of words in it ")
# print(len(s.split()))

# # Replace all spaces in a string with hyphens (-).
# s = input("Enter a string to join string with -: ")
# print(s.replace(" ", "-"))

# # Remove all special characters from a string.
# import string

# s = input("Enter a string to remove all the special characters in it: ")
# final_string_without_special_characters = "".join(
#     char for char in s if char not in string.punctuation
# )
# print(final_string_without_special_characters)

# Find the longest word in a sentence.
s = input("Enter a string to find the longest word in it: ")
words = s.split()
print(max(words, key=len) if len(words) > 0 else False)

# Check if two strings are anagrams.
s = input("Enter two space-separated words to check if they are anagrams: ")
words = s.split()

if len(words) == 2:
    str1 = words[0].lower()
    str2 = words[1].lower()

    if sorted(str1) == sorted(str2):
        print("They are anagrams.")
    else:
        print("They are not anagrams.")
else:
    print("Please enter exactly two words separated by space.")
