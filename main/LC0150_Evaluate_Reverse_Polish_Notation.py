from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            try:
                num = int(token)
                stack.append(num)
            except ValueError:
                secondOperand = stack.pop()
                firstOperand = stack.pop()

                result = 0

                if token == '+':
                    result = firstOperand + secondOperand
                elif token == '-':
                    result = firstOperand - secondOperand
                elif token == '*':
                    result = firstOperand * secondOperand
                elif token == '/':
                    result = int(firstOperand / secondOperand)

                stack.append(result)

        return stack[0]