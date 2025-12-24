## 1 Reverse of a given number and palindrome
def getReverse(number):
    temp = number
    reverseNumber = 0
    while temp > 0:
        rem = temp % 10
        reverseNumber = reverseNumber*10 + rem
        temp //= 10
    return reverseNumber

num = int(input()) # ip from user
if(num == getReverse(num)):
    print("Given number is palindrome")
else:
    print("Given number is not a palindrome")
