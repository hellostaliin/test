def moveZeroes(nums):
    for i in range(nums.count(0)):
        nums.append(nums.pop(nums.index(0)))
nums = [0]
moveZeroes(nums)


