class Stack(object):
    def __init__(self):
        self.stack = []
    
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        
        return None
    
    def pop(self):
        self.stack.pop()
    
    def push(self, index):
        self.stack.append(index)
    
    def isCurrentStackIndexSonner(self, value):
        # Case: Current stack is empty
        if self.peek() == None:
            return False
        
        if value == None:
            # Case: Other stack is empty. Current stack contains value(s)
            if self.peek() != None:
                return True

        
        if value != None and self.peek() != None:
            return self.peek() < value

class Solution(object):
    def nSquared(self, nums):
        best = -10 * 2 * 10 **4
        for i in range(len(nums)):
            product = 1
            for j in range(i, len(nums)):
                product *= nums[j]
                best = max(product, best)
        return best
    
    def n(self, nums):
        # Edge Case: len(0)
        if len(nums) == 0:
            return 0
        # Edge Case: len(1)
        if len(nums) == 1:
            return nums[0]

        # 1. Populate stacks
        negativeStack = Stack()
        zeroStack = Stack()
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                zeroStack.push(i)
            elif nums[i] < 0:
                negativeStack.push(i)
        
        print(negativeStack.stack, zeroStack.stack)

        # 2. Loop over array
        best = 0 # FIXME: zero edge case
        current = 0
        for i in range(len(nums)):
            if current == 0:
                current = nums[i]
            elif current > 0:
                current *= nums[i]
            elif current < 0:
                if negativeStack.isCurrentStackIndexSonner(zeroStack.peek()):
                    current *= nums[i]
                else:
                    current = nums[i]

            if negativeStack.peek() == i:
                negativeStack.pop()
            if zeroStack.peek() == i:
                zeroStack.pop()
            best = max(best, current)
        

        return best

    def nAgain(self, nums):
        best = max(nums)
        minmax = {'min': 1, 'max': 1}

        for n in nums:
            if n == 0:
                minmax['max'] = 1
                minmax['min'] = 1
                continue
            
            maxn = minmax['max'] * n
            minmax['max'] = max(maxn, minmax['min'] * n, n)
            minmax['min'] = min(maxn, minmax['min'] * n, n)
            best = max(best, minmax['max'])
        return best

    
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.nAgain(nums)
