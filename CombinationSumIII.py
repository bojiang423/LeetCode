# Combination Sum III

'''
Find all possible combinations of k numbers that add up to a number n, 
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''

###############################################################
# My solution                                                 #
# Run time   :  8960 ms                                       #
# Memory Used:  13.8 MB                                       #
###############################################################
num_list = [1,2,3,4,5,6,7,8,9]

def getSubList(k,n):

    sum_list = []

    if k == 1:
        if n > 9:
            return []
        sum_list.append([n])
    else:
        for i in range(1,n//2+2):
            if (n-i) <= sum(num_list[1-k:]) and (n-i) > 0:
                for lst in (getSubList(k-1, n-i)):
                    if i < lst[0]:
                        sum_list.append([i] + lst)

    return sum_list

print(f'{getSubList(9,45)}')


###############################################################
# Fast solution - 12 ms                                       #
###############################################################
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        res = []
        self.dfs(range(1,10), k, n, 0, [], res)
        return res

    def dfs(self, nums, k, n, index, path, res):
        if k < 0 or n < 0: # backtracking 
            return 
        if k == 0 and n == 0: 
            res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, k-1, n-nums[i], i+1, path+[nums[i]], res)
'''
###############################################################
# Fast solution - 16 ms                                       #
###############################################################
'''
class Solution:

    def dfs(self, idx, result, size, target, temp):
        if len(temp) == size and target == 0:
            result.append(temp[:])
            return

        for i in range(idx, 10):
            if i > target:
                break
            temp.append(i)
            self.dfs(i + 1, result, size, target - i, temp)
            temp.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.dfs(1, result, k, n, [])
        return result
'''
###############################################################
# Fast solution - 24 ms                                       #
###############################################################
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        cmb = []
        def backtrack(k, n, start):
            if k==0:
                if n == 0:
                    res.append(cmb[:])
                else:
                    return
            else:
                for i in range(start, 10):
                    if i > n:
                        return
                    cmb.append(i)
                    backtrack(k-1,n-i,i+1)
                    cmb.pop()
        backtrack(k,n,1)
        return res
'''