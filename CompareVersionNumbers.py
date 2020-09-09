# Compare Version Numbers
'''
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.

The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and fourth level revision number are both 0.

Example 1:

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Example 2:

Input: version1 = "1.0.1", version2 = "1"
Output: 1
Example 3:

Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
Example 4:

Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both “01” and “001" represent the same number “1”
Example 5:

Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: The first version number does not have a third level revision number, which means its third level revision number is default to "0"
 

Note:

Version strings are composed of numeric strings separated by dots . and this numeric strings may have leading zeroes.
Version strings do not start or end with dots, and they will not be two consecutive dots.

'''

##########################################
# Solution 1                             #
# 72 / 72 test cases passed.             #
# Runtime: 28 ms (> 80.87%)              #
# Memory Usage: 13.9 MB  (> 39.53%)      #
##########################################

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        

        v1 = list(map(int, version1.split('.'))) 
        v2 = list(map(int, version2.split('.')))
        
        print(v1)
        print(v2)
        
        version_len = max(len(v1), len(v2))
        
        if len(v1) < version_len:
            for i in range(version_len - len(v1)):
                v1.append(0)
                
        if len(v2) < version_len:
            for i in range(version_len - len(v2)):
                v2.append(0)
        
        for i in range(version_len):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1                
                
        return 0

##########################################
# Fast solution - 12 ms                  #
##########################################
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1, l2 = version1.split('.'), version2.split('.')
        n1, n2 = len(l1), len(l2)
        
        i = 0
        for i in range(max(n1, n2)):
            val1 = int(l1[i]) if i < n1 else 0
            val2 = int(l2[i]) if i < n2 else 0
            if val1 != val2:
                return 1 if val1 > val2 else -1
            # if val1 > val2:
            #     return 1
            # elif val1 < val2:
            #     return -1
        return 0

##########################################
# Solution using less memory - 13516 KB  #
##########################################

from itertools import zip_longest

class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        versions1 = list(map(int, version1.split(".")))
        versions2 = list(map(int, version2.split(".")))
        
        for v1, v2 in zip_longest(versions1, versions2, fillvalue=0):            
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
            
        return 0