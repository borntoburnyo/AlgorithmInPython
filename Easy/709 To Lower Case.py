Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"

class Solution:
  def toLowerCase(self, str):
    """
    type str: str
    rtype: str
    """
    ord_gap = ord('a') - ord('A') + 26 - 1
    result = []
    
    for ord_str in [ord(s) for s in str]:
      if ord_str <= ord('Z'):
        result.append(chr(ord_str + ord_gap))
      else:
        result.append(chr(ord_str))
    
    return ''.join(result)

#test
string = 'HeLLo'
Solution().toLowerCase(string)
