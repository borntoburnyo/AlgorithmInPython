class Solution:
    def expand(self, s):
        self.res = []
        def helper(s, word):
            if not s:
                self.append(word)
            else:
                if s[0] == "{":
                    i = s.find("}")
                    for letters in s[1:i].split(","):
                        helper(s[i+1:], word+letter)
                else:
                    helper(s[1:], word+letter)
        helper(s, "")
        self.res.sort()
        return self.res
