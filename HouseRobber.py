# House Robber

'''
Example 1:
nums = [3,1,3,15,8], output = 19

Example 2:
input = [1,2,3,1], output = 4

Example 3:
input = [2,7,9,3,1], output = 12

Example 4:
input = [], output = 0

Example 5:
input = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
output = 
'''

########################################
# My Solution 1 - Take too much time   #
########################################
'''
def rob1(nums):

    result = 0
    for i in range(len(nums)):
        left_max = right_max = 0
        if i > 1:
            left_max = rob1(nums[:i-1])
        if (i+2) >= len(nums):
            right_max = rob1(nums[i+2:])
        temp = nums[i] + left_max + right_max
        if temp > result:
            result = temp

    return result
'''
##################################################################
# My Solution 2 - much faster than 1, but still too slow         #
##################################################################
'''
def rob2(nums):

    if len(nums) == 0:
        return 0

    last_idx = len(nums) - 1
    result = 2

    def getSum(i, curr_max):
        if i > last_idx:
            result = 3
            return curr_max
        else:
            new_max = curr_max + nums[i]
            max1 = getSum(i+2, new_max)
            max2 = getSum(i+3, new_max)
            return max(max1, max2)

    return max(getSum(0,0), getSum(1,0))
'''
##################################################################
# My Solution 3 - (first accepted solution)                      #
# 69 / 69 test cases passed.                                     #
# Runtime: 28 ms  (> 84.77%)                                     #
# Memory Usage: 13.9 MB (> 48.13%)                               #
##################################################################
def rob3(nums):

    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    result = 0
    sum_dict = {}

    for i in range(len(nums)):

        max1 = max2 = 0
        if i - 2 >= 0:
            max1 = sum_dict[i-2]
        if i - 3 >= 0:
            max2 = sum_dict[i-3]
        sum_dict[i] = max(max1, max2) + nums[i]

    result = max(sum_dict[len(nums)-1], sum_dict[len(nums)-2])

    return result
##################################################################
# My Solution 4 - upgrade from solution 3                        #
# 69 / 69 test cases passed.                                     #
# Runtime: 40 ms  (> 27.57%) should be faster, try submit later  #
# Memory Usage: 13.9 MB (> 48.13%)                               #
##################################################################
def rob4(nums):

    max1 = max2 = max3 = 0
    
    # (max1, max2, max3, num...)
    for num in nums:
        temp = max(max1, max2) + num
        max1 = max2
        max2 = max3
        max3 = temp

    return max(max2, max3)


#house_nums = [226,174,214,16,218,48,153,131,128,17,157,142,88,43,37,157,43,221,191,68,206,23,225,82,54,118,111,46,80,49,245,63,25,194,72,80,143,55,209,18,55,122,65,66,177,101,63,201,172,130,103,225,142,46,86,185,62,138,212,192,125,77,223,188,99,228,90,25,193,211,84,239,119,234,85,83,123,120,131,203,219,10,82,35,120,180,249,106,37,169,225,54,103,55,166,124]
#house_nums = [155,44,52,58,250,225,109,118,211,73,137,96,137,89,174,66,134,26,25,205,239,85,146,73,55,6,122,196,128,50,61,230,94,208,46,243,105,81,157,89,205,78,249,203,238,239,217,212,241,242,157,79,133,66,36,165]
#house_nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
#house_nums = [183,219,57,193,94,233,202]
#house_nums = [2,7,9,3,1]
house_nums = []
print(f'{house_nums}, max money {rob4(house_nums)}')

##################################################################
# Fastest Solution (8 ms)                                        #
##################################################################
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
'''