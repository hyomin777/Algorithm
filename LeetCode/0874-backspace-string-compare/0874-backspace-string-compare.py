class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1, stack2 = [], []

        def build_stack(stack, s):
            for char in s:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
        
        build_stack(stack1, s)
        build_stack(stack2, t)

        if stack1 == stack2:
            return True
        else:
            return False
        