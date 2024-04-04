class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxLength = 0

        for c in s:
            if c == "(":
                stack.append(c)
                maxLength = max(maxLength, len(stack))
            elif c == ")":
                stack.pop()

        return maxLength