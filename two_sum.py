def two_sum(nums, target):
    if not nums:
        return 0

    output=[]
    for i in range(1, len(nums)):
        if (nums[i-1]+nums[i])==target:
            output.extend([i-1, i])
    return output

r=two_sum([2,7,11,15], 26)
print(r)