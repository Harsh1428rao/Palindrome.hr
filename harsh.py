# Palindrome.hr
#Its a palindrome code which is very simple to understand
a=input()
len(a)
b=a[0]
c=a[len(a)-1]
if (b==c) and a==a[::-1]:
    print("It is a Palindrome")
else:
    print("It is not Palindrome ")
