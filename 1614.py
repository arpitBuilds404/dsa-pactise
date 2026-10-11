class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maximum = 0

        for i in s:
            if i == "(":
                count += 1
                if count > maximum:
                    maximum = count
            elif i == ")":
                count -= 1

        return maximum