# Robot Bounded In Circle


####################################################################################
# My First Accepted Solution (use numpy may take more time and memory)             #
# 110/110 cases passed                                                             #     
# Runtime: 92ms                                                                    #
# Memory Usage: 29.5 MB                                                            #
####################################################################################
import numpy as np

def isRobotBounded(instructions):
    old_position = np.array([0,0])
    new_position = np.array([0,0])
    direction = np.array([[0,1],[-1,0],[0,-1],[1,0]])
    direction_desc = ['North','West','South','East']
    old_direction_idx = new_direction_idx = 0

    for ins in instructions:
        print(f'{new_position}, {direction_desc[new_direction_idx]}')
        if ins == 'G':
            new_position = new_position + direction[new_direction_idx]
        elif ins == 'L':
            new_direction_idx = (new_direction_idx + 1)%4
        else:
            new_direction_idx = (new_direction_idx - 1)%4 

    if np.array_equal(new_position, old_position):
        return True

    if old_direction_idx != new_direction_idx:
        return True

    return False

#instructions = 'GGLLGG'    # True
#instructions = 'GG'        # False
#instructions = 'GL'        # True
#instructions = "GLRLLGLL"   # True
instructions = "LRRRRLLLRL"  # True
#instructions = "RRGRRGLLLRLGGLGLLGRLRLGLRLRRGLGGLLRRRLRLRLLGRGLGRRRGRLG"   # False

print(f'{instructions} => {isRobotBounded(instructions)}')

####################################################################################
# Fastest Solution 12ms
####################################################################################
'''
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        go = {'N':(0,1), 'S':(0,-1), 'W':(-1,0), 'E':(1,0)}
        left = {'N':'W', 'W':'S', 'S':'E', 'E':'N'}
        right = {'N':'E', 'E':'S', 'S':'W', 'W':'N'}
        current = [0, 0]
        direction = 'N'
        
        for i in instructions:
            if i == 'G':
                x, y = go[direction]
                current[0] += x
                current[1] += y
            elif i == 'L':
                direction = left[direction]
            else:
                direction = right[direction]
        
        if current == [0,0] or direction != 'N':
            return True
        else:
            return False
'''