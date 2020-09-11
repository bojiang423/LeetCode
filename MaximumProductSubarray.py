### Maximum Product Subarray


###############################################
# Solution 1                                  #
# 187 / 187 test cases passed.                #
# Runtime: 8212 ms                            #
# Memory Usage: 13.8 MB                       #
###############################################

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxProduct = 0
        
        if len(nums) == 1:
            return nums[0]
        
        for i in range(len(nums)):
            product = nums[i]
            if product > maxProduct:
                maxProduct = product
            if i < len(nums)-1:
                for j in range(i+1, len(nums)):
                    product = product * nums[j]
                    if product > maxProduct:
                        maxProduct = product
                    
        return maxProduct

###############################################
# Fastest Solution 1  (36 ms)                 #
###############################################
class Solution1:
    def maxProduct(self, nums: List[int]) -> int:
        max_num = min_num = 1
        max_product = float('-inf')
        for num in nums:
            num1 = max_num * num
            num2 = min_num * num
            max_num = max(num, num1, num2)
            min_num = min(num, num1, num2)
            max_product = max(max_product, max_num)
        return max_product
###############################################
# Fastest Solution 2                          #
###############################################
class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return nums[0]
        if 0 in nums:
            nums = self.splitByZero(nums)
            products = []
            
            for arr in nums:
                products.append(self.maxProductNoZeros(arr))
                
            products.append(0)
            print(products)
            return max(products)
        else:
            return self.maxProductNoZeros(nums)
            
    def splitByZero(self, nums):
        retArr = [] #2d array
        row = []
        for num in nums:
            if num == 0:
                if len(row) > 0:
                    retArr.append(row)
                    row = []
            else:
                row.append(num)
        if len(row) > 0:
            retArr.append(row)
        return retArr
    
    def maxProductNoZeros(self, nums):        
        if (len(nums) == 1):
            return nums[0]
        
        countNeg = 0
        for num in nums:
            if num < 0:
                countNeg += 1
                
        if (countNeg % 2) == 0:
            #include whole array
            prod = 1
            for num in nums:
                prod *= num
            return prod
        
        #odd number of negatives in array - find whether we should eliminate the last or the first
        elimFirstProd = 1
        i = 0
        while nums[i] > 0 and i < len(nums):
            i += 1
        while i < len(nums)-1:
            i += 1
            elimFirstProd *= nums[i]
            
            
        elimLastProd = 1
        i = len(nums)-1
        while (nums[i] > 0) and i >= 0:
            i -= 1
        while i > 0:
            i -= 1
            elimLastProd *= nums[i]
            
            
        return max(elimFirstProd, elimLastProd)


