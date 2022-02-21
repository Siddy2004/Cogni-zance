# QUESTION-4

# PROGRAM TO CHECK IF A GIVEN NUMBER IS A PALINDROME NUMBER

num1 = int(input("Enter any number:"))
temp = str(num1)
pal  = ""

for i in range(len(temp)):
    pal = temp[i] + pal

num2 = int(pal)
if num1 == num2:
    print(num1, "is a palindrome number")
else:
    print(num1, "is not a palindrome number")


