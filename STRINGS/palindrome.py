str = input("Enter a string:")
rev = ""
for i in str:
    rev = i + rev
print(rev)
if rev == str:
    print("Palindrome")
else:
    print("Not a Palindrome")