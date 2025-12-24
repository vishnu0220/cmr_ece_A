## Move all zeros to the end

n = int(input())

nums = []

for i in range(n):
    ele = int(input())
    nums.append(ele)

## Code for the task
nonZeros = []
zeros = []

for i in nums:
    if i != 0:
        nonZeros.append(i)
    else:
        zeros.append(i)

res = nonZeros + zeros
print(res)