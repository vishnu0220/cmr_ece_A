## 4 Sum of odd index values minus Sum of even index values
def getResult(nums):
    evenSum = 0
    oddSum = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            evenSum += nums[i]
        else:
            oddSum += nums[i]
    print("Even sum : ", evenSum)
    print("Odd sum : ", oddSum)
    return evenSum - oddSum

n = int(input())
nums = []
for i in range(n):
    ele = int(input())
    nums.append(ele)

print(getResult(nums))