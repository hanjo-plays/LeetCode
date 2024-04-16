class Solution(object):
    def primePalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n>2*10**8:
            return -1
        for i in range (n, 2*10**8):
            if i == int(str(i)[::-1]) and self.isprime(i):
                
                return i
        return -1
            
    
    def isprime(self, n):
        if n<=3:
            return True
        if n % 2==0 or n % 3 == 0:
            return False
        for i in range(5, int(n**0.5)+1,6):
            if n % i == 0 or n % (i+2) == 0:
                return False
        return True
      
a = Solution()  
x=a.primePalindrome(6)
print(x)
Change?