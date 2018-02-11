class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        total = 0
        while n != 0:
            n = n // 5
            total = total + n
        return total

a = Solution()
print(a.trailingZeros(100))

