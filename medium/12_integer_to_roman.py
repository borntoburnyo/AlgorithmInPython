class Solution:
    def intToRoman(self, num):
        # Initialize the int-to-roman map
        integers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        romans = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

        res = ""

        # Imagine 900 = 0*1000 + 1*900
        for k, v in enumerate(integers):
            res += (num // v) * romans[k]
            num %= v

        return res
