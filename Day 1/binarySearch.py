## [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
##   0   1   2   3   4   5   6   7   8    9

## target = 45

n = int(input())
nums = []
for i in range(n):
    ele = int(input())
    nums.append(ele)
target = int(input("Enter target to find : "))

# Binary search Algo

low = 0
high = len(nums)-1
targetFound = False
while low <= high:
    mid = (low+high)//2
    if nums[mid] == target:
        targetFound = True
        print("Target is found")
        break
    elif nums[mid] < target:
        low = mid+1
    else:
        high = mid-1

if(targetFound == False):
    print("Target not found")
