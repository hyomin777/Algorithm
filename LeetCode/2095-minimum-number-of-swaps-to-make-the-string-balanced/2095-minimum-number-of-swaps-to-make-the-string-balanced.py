class Solution:
    def minSwaps(self, s: str) -> int:
        stack=[]
        cnt = 0

        for char in s:
            if char == '[':
                stack.append(char)
            else:
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    cnt += 1
        return (cnt + 1) // 2