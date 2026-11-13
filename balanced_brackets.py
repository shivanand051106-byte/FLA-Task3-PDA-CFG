# Pushdown Automaton for Balanced Brackets

class BalancedBracketsPDA:
    def validate(self, expr: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in expr:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        
        return len(stack) == 0
