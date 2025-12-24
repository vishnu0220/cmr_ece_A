## Find the missing number, where you will have all numbers from 1 to n but one will be missing
n = int(input())
nums = []
for i in range(n-1):
    ele = int(input())
    nums.append(ele)

## see you will have numbers from 1 to n, but list size is actually n-1
## but you will store only n-1 elements in the list

## Task to get the answer

sum = (n)*(n+1)//2
print("sum: ", sum)
arraySum = 0
for i in nums:
    arraySum += i
print(arraySum)
print("Missing number : ", sum-arraySum)