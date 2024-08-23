import re


class Solution:
    def fractionAddition(self, expression: str) -> str:
        if expression[0].isdigit():
            expression = "+" + expression

        split_expression = re.findall(r"[^-+]+|[-+]", expression)
        print(split_expression)

        while len(split_expression) >= 4:
            left = [split_expression[0]] + split_expression[1].split("/")
            right = [split_expression[2]] + split_expression[3].split("/")

            denominator = int(left[2]) * int(right[2])
            numerator = (1 if left[0] == '+' else -1) * int(left[1]) * int(right[2])
            numerator += (1 if right[0] == '+' else -1) * int(left[2]) * int(right[1])

            while True:
                isDividable = False
                for i in range(2, denominator + 1):
                    if numerator % i == 0 and denominator % i == 0:
                        numerator = int(numerator / i)
                        denominator = int(denominator / i)
                        isDividable = True
                        break

                if not isDividable:
                    break

            split_expression = ["+" if numerator >= 0 else "-"] + [
                f"{abs(numerator)}/{denominator}"] + split_expression[4:]

        split_expression = split_expression[1:] if split_expression[0] == "+" else split_expression

        return "".join(split_expression)
