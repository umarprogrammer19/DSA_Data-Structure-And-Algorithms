# Check if a string is a palindrome.
string = input("Enter a string to check a palindrome: ")
if string == string[::-1]:
    print(string, "is Palindrome")
else:
    print(string, "is not Palindrome")

# Count vowels and consonants in a string.
string2 = input("Enter a string to count the vowels and consonants: ")
vowels = ["a", "e", "i", "o", "u"]
vov, cons = 0, 0

for val in string2:
    if val.lower() in vowels:
        vov += 1
    elif val.isalpha():
        cons += 1

print("Vowels:", vov)
print("Consonants:", cons)
