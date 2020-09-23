# Majority Element II

'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.
'''

#############################################################
# 66 / 66 test cases passed.
# Status: Accepted
# Runtime: 116 ms (> 92.26%)
# Memory Usage: 15 MB (> 33.40%)
#############################################################
def majorityElement(nums):

    result = []

    min_apperance = len(nums)//3

    nums.sort()

    curr_num = nums[0]
    curr_count = 1

    print(nums)
    print(min_apperance)
    for i in range(1, len(nums)):
        if nums[i] == curr_num:
            curr_count = curr_count + 1
        else:
            if curr_count > min_apperance:
                result.append(curr_num)
            curr_num = nums[i]
            curr_count = 1

    if curr_count > min_apperance:
        result.append(curr_num)

    return result 


nums_01 = [3,2,3]
expected_01 = [3]

nums_02 = [1,1,1,3,3,2,2,2]
expected_02 = [1,2]

nums = nums_02
print(f'nums : {nums}, majority elements {majorityElement(nums)}')

#############################################################
# Fastest solution (92 ms)
#############################################################
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2)
                        if nums.count(n) > len(nums) // 3]
'''