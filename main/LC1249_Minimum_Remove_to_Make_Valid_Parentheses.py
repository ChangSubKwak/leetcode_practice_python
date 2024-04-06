class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        index = []

        for i, c in enumerate(s):
            if c.isalpha():
                continue

            if c == '(':
                stack.append(c)
                index.append(i)
                continue

            if c == ')' and len(stack) > 0 and stack[-1] == '(':
                stack.pop()
                index.pop()
                continue

            index.append(i)

        result = ""
        for i, c in enumerate(s):
            if i in index:
                continue
            result += c

        return result
