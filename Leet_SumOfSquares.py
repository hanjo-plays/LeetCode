' The first one does not work for large numbers, the second one is the correct one.'
# class Solution(object):
#     def judgeSquareSum(self, c):
#         """
#         :type c: int
#         :rtype: bool
#         """
#         for a in range(0,int(c**0.5)+1):
#             #print("a",a)
#             for b in range(int(c**0.5),-1,-1):
#                 #print("b",b)
#                 if a**2+b**2==c:
#                     #print(a,b)
#                     return True
#         return False
    
# print(Solution().judgeSquareSum(999999999))

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a = 0
        b = int(c ** 0.5)
        
        while a <= b:
            current_sum = a**2 + b**2
            if current_sum == c:
                return True
            elif current_sum < c:
                a += 1
            else:
                b -= 1
        #print("False")        
        return False

print(Solution().judgeSquareSum(999999999))
