class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = [*str(x)]
        total = 0

        for i in s:
            total += int(i)

        if x % total == 0:
            return total
        return -1
