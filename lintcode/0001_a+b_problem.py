# Write a function that add two numbers A and B.
# You should not use + or any arithmetic operators.

class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        while b != 0:
            _a = a ^ b
            _b = (a & b) << 1
            a = _a
            b = _b

        return a


