# Largest Number
'''
Given a list of non negative integers, arrange them such that they form the largest number.
'''
################################################################################
# My solution (traditional way, the fastest solution at the bottom is amazing)
# 222 / 222 test cases passed.
# Status: Accepted
# Runtime: 96 ms
# Memory Usage: 14.1 MB
################################################################################
def largestNumber(nums):

    output = ""

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (str(nums[i]) + str(nums[j])) < (str(nums[j]) + str(nums[i])):
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
        output = output + str(nums[i])

    if int(output) == 0:
        return "0"

    return output  

##########################################################
nums_01 = [10,2]
expected_01 = "210"

nums_02 = [3,30,34,5,9]
expected_02 = "9534330"

nums_03 = [0,0]
expected_03 = "0"

nums = nums_03
expected = expected_03
output = largestNumber(nums)

print(f'Input  : {nums}')
print(f'Output : {output}')
print(f'Expcted: {expected}')

##########################################################
# Fastest solution (20ms)
##########################################################
'''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(x, y):
            u = x + y
            v = y + x
            if u == v:
                return 0
            elif u < v:
                return -1
            else:
                return 1

        v = map(str, nums)
        result = ''.join(reversed(sorted(v, key=cmp_to_key(cmp))))
        if result and result[0] == '0':
            return '0'
        else:
            return result
'''