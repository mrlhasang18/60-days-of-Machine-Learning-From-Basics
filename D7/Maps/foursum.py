
def fourSum(nums, target):
    nums.sort()
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sum_two = nums[i] + nums[j]
            diff = target - sum_two
            two_sum_dict = {}
            for k in range(j + 1, len(nums)):
                if nums[k] in two_sum_dict:
                    quadruplet = [nums[i], nums[j], nums[k], two_sum_dict[nums[k]]]
                    quadruplet.sort()
                    if quadruplet not in result:
                        result.append(quadruplet)
                two_sum_dict[diff - nums[k]] = nums[k]
    return result

# Test the function
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))  

#test2
nums = [2, 2, 2, 2, 2]
target = 8
print(fourSum(nums, target))

