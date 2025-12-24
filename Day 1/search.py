## 2 Searching in the list
def isPresent(nums, tar):
    for i in nums:
        if i == tar:
            return True
    return False

n = int(input()) # Takes ip from the user
nums = []

for i in range(n):
    ele = int(input())
    nums.append(ele)

tar = int(input("Enter target value : "))
print(isPresent(nums, tar))