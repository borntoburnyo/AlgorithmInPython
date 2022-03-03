class Solution:
    # Use Tuple(string) to identify anagrams
    def groupAnagrams(self, strs):
        res = {}
        for x in strs:
            key = tuple(sorted(x))
            res[key] = res.get(key, []) + [x]
        return res.values()

    # Use character count to identify anagrams
    def v2(self, strs):
        res = {}
        for x in strs:
            count = [0]*26
            for c in x:
                count[ord(c) - ord('a')] += 1
            res[tuple(c)] = res.get(tuple(c), []) + [x]
        return
