The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

class Solution:
  def hammingDistance(self, x, y):
    xb, yb = format(x, 'b'), format(y, 'b')
    if len(xb) < len(yb):
      xb = '0'*(len(yb) - len(xb)) + xb
    if len(xb) > len(yb):
      yb = '0'*(len(xb) - len(yb)) + yb
    else:
      pass
    
    return sum([i != j for i,j in zip(xb, yb)])
    
   
