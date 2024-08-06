class Calculator:

    def sum(selrf, a, b):
        result = a+b
        return result
    
    def sub(self, a, b):
        result = a-b
        return result
    
    def mul(self, a, b):
        return a*b
    
    def dev(self, a, b):
        if b == 0:
            raise ArithmeticError("на ноль делить нельзя")
        return a/b
    
    def pow(self, a, b=2):
        return a**b
    
    def avg(self, nums):
        if (len(nums) == 0):
            return 0

        s = 0
        for num in nums:
             s = s + num

        l = len(nums)
        return self.dev(s, l)
