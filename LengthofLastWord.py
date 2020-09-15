# Length of Last Word
'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.
'''

##################################################################
# My solution (first accepted)                                   #
# 59/59 test cases accepted                                      #
# Runtime: 24 ms  (> 93.20%)                                     #
# Memory Usage: 13.9 MB  (> 41.87%)                              #
##################################################################
def lengthOfLastWord(s):

    l = s.split(' ')
    print(l)
    l2 = [x for x in l if x!='']
    print(l2)
    if len(l2) > 0:
        return len(l2[-1])
    return 0

#s = "a "
s = "Hello World"
#s = "Hello"
#s = ' '
#s = ''

print(f's = {s}, length of last word {lengthOfLastWord(s)}')

##################################################################
# Fastest solution (12 ms)                                       #
##################################################################
'''
import re
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        return len(re.split('\s+', s.strip())[-1])
'''