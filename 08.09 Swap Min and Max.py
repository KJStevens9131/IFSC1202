str = input("Enter Values Seperated by Spaces: ")
nums = (list(str.split(" ")))
nums = [int(nums[k]) for k in range(len(nums))]
n = len(nums)
minn = 0
maxx = 0
for i in range(n):
    if nums[i]<nums[minn]:
        minn = i
    if nums[i]>nums[maxx]:
        maxx = i

nums[minn], nums[maxx] = nums[maxx], nums[minn]

print("Swapped minimum and maximum:",end=" ")
for j in range(n):
    print(nums[j],end=" ")