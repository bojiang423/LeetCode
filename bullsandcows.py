# Bulls and Cows
'''
You are playing the following Bulls and Cows game with your friend: 
You write down a number and ask your friend to guess what the number is. 
Each time your friend makes a guess, you provide a hint that indicates 
how many digits in said guess match your secret number exactly in both 
digit and position (called "bulls") and how many digits match the secret 
number but locate in the wrong position (called "cows"). Your friend will 
use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's 
guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

Test Cases
1) "1807" "7810" ==> 1A3B
    1#07   7#10 
2) "1122" "2211" ==> 0A4B
3) "1"    "0"    ==> 0A0B
4) "1122" "1111" ==> 2A0B
    ##22   ##11 
5) "1123" "0111" ==> 1A1B
    1#23   0#11
6) "1111" "1122" ==> 2A0B
    ##11   ##22 
7) "1122" "2210" ==> 0A3B

Bulls:
- same position, same value

Cows:
- Match value but wrong position
'''

##################################################
# Solution 1                                     #
# 152 / 152 test cases passed.                   #
# Runtime: 80 ms                                 #
# Memory Usage: 13.8 MB                          #
##################################################
def getHint(secret: str, guess: str) -> str:
    
    bulls = cows = 0

    sec2 = []
    gus2 = []
    
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls = bulls + 1
        else:
            sec2.append(secret[i])
            gus2.append(guess[i])
    
    #print("sec2 {}, gus2 {}".format(sec2, gus2))

    for i in range(len(sec2)):
        if sec2[i] in gus2:
            cows = cows + 1
            gus2.remove(sec2[i])
    
    return str(bulls) + "A" + str(cows) + "B"

##################################################
# Fastest Solution                               #
# Runtime: 80 ms                                 #
##################################################
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        bull=0
        for i in range(len(secret)):
            bull += int(secret[i] == guess[i])
        
		# This loop will take care of "cow" cases
        cows=0
        for c in set(secret):
            cows += min(secret.count(c), guess.count(c))
        
        return f"{bull}A{cows-bull}B"

if __name__ == "__main__":

    group = [['1807','7810'],['1122','2211'],['1','0'],['1122','1111'],['1123','0111'],['1111','1122']]
    '''
    1) "1807" "7810" ==> 1A3B
    2) "1122" "2211" ==> 0A4B
    3) "1"    "0"    ==> 0A0B
    4) "1122" "1111" ==> 2A0B
    5) "1123" "0111" ==> 1A1B
    6) "1111" "1122" ==> 2A0B
    '''
    for a in group:
        print("Secret {}, Guess {}, Hint: {}".format(a[0], a[1], getHint(a[0],a[1])))