ROUND_BRACKET_OPEN = '('
SQUARE_BRACKET_OPEN = '['
CURLY_BRACKET_OPEN = '{'
ROUND_BRACKET_CLOSE = ')'
SQUARE_BRACKET_CLOSE = ']'
CURLY_BRACKET_CLOSE = '}'

class InvalidBracketException(Exception):
    pass

class BracketStack:
    def __init__(self):
        self.stack = []
    
    # edge case: ] or } or ) to start
    def peak(self):
        if len(self.stack) == 0:
            return None

        return self.stack[-1]

    def pop(self, data):
        if data == ROUND_BRACKET_CLOSE and self.peak() != ROUND_BRACKET_OPEN:
            raise InvalidBracketException()
        if data == SQUARE_BRACKET_CLOSE and self.peak() != SQUARE_BRACKET_OPEN:
            raise InvalidBracketException()
        if data == CURLY_BRACKET_CLOSE and self.peak() != CURLY_BRACKET_OPEN:
            raise InvalidBracketException()
        
        self.stack.pop()
    
    def push(self, bracket):
        if bracket in [ROUND_BRACKET_CLOSE, SQUARE_BRACKET_CLOSE, CURLY_BRACKET_CLOSE]:
            self.pop(bracket)
        else:
            self.stack.append(bracket)

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = BracketStack()
        for bracket in s:
            try:
                stack.push(bracket)
            except InvalidBracketException:
                return False

        if len(stack.stack) > 0:
            return False

        return True
