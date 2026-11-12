class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        for _ in range(32):
            if not b: break

            a, b = a ^ b, (a & b) << 1
        
        if b:
            return a & 0xFFFFFFFF
        
        return a


'''
1010101
0011010

    111
'''