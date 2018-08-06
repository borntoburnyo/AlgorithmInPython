Initially, there is a Robot at position (0, 0). Given a sequence of its moves, 

judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. 

The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false

class Solution:
  def judgeCircle(self, moves):
    if len(set([c for c in moves])) % 2 == 1 or len(moves) == 1:
      return False
    else:
      moves = [c for c in moves]
      mdict = {c: moves.count(c) for c in ['U','D','L','R']}
      
    return mdict['U'] == mdict['D'] and mdict['L'] == mdict['R']
    
    
class Solution:
  def judgeCircle(self, moves):
    return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')
 
 
