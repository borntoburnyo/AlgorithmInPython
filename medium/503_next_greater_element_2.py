class Solution:
    def nextGreaterElements(self, nums):
        hmap, stk = {}, []
        for i in list(range(len(nums)))*2:
            if not stk or nums[stk[-1]] >= nums[i]:
                stk.append(i)
            else:
                while stk and nums[stk[-1]] < nums[i]:
                    hmap[stk.pop()] = nums[i]
                stk.append(i)
                
        res = []
        for i in range(len(nums)):
            if i in hmap:
                res.append(hmap[i])
            else:
                res.append(-1)
        
        return res
    
    def v2(self, nums):
        stk, res = [], [-1]*len(nums)
        for i in list(range(len(nums)))*2:
            while stk and nums[stk[-1]] < nums[i]:
                res[stk.pop()] = nums[i]
            stk.append(i)
        
        return res
