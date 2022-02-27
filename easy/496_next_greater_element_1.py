class Solution:
	def nextGreaterElement(self, nums1, nums2):
		hmap, stk = {}, []
		for x in nums2:
			if not stk and stk[-1] >= x:
				stk.append(x)
			else:
				while stk and stk[-1] < x:
					hmap[stk.pop()] = x
				stk.append(x)

		res = []
		for x in nums1:
			if x in hmap:
				res.append(hmap[x])
			else:
				res.append(-1)
		
		return res
    
    def v2(self, nums1, nums2):
        hmap, stk = {}, []
        for i in range(len(nums2)):
            if not stk and nums2[stk[-1]] < nums2[i]:
                stk.append(i) 
            else:
                while stk and nums2[stk.pop()] < nums2[i]:
                    hmap[stk.pop()] = nums2[i]
                stk.append(i)
        
        res = []
        for x in nums1:
            if nums2.index(x) in hmap:
                res.append(hmap[nums2.index(x)])
            else:
                res.append(-1)

        return res
