class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        digits_str=str(x)
        
        if digits_str[0]=="-":
            
            
            digits_str=digits_str[1:] # remove the negative sign using slicing
            digits_str_reversed = digits_str[::-1] # reverse the string using slicing
            digits_str_reversed = "-" + digits_str_reversed
        
        else:
        
            digits_str_reversed = digits_str[::-1]
        
        digits_str_reversed=int(digits_str_reversed)        
      
        if digits_str_reversed>=(-2**31) and digits_str_reversed<=((2**31) - 1):
            return digits_str_reversed
        else:
            return 0

print(-2**31)
print(Solution().reverse(-2147483648))