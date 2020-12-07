class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n==1: return 1
        # if n==2: return 2
        # return self.climbStairs(n-1)+ self.climbStairs(n-2)
        return self.fibonacci(n)
    def fibonacci(self, n):
        if n==1: return 1
        if n==2: return 2
        prev = 1
        curr = 2
        for i in range(n-2):
            curr, prev = prev + curr, curr
            
        return(curr)
            
