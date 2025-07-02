# Check if a string is a palindrome.
string = input()
if string == string[::-1]:
    print(string, "is Palindrome")
else:
    print(string, "is not Palindrome")
