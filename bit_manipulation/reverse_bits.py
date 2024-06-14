class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            least = n&1
            n>>=1
            ans = ans <<1
            ans = ans | least
        return ans
