class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0]
        for i in range(1,n+1):
            arr.append(arr[i>>1]+i%2)#i divided by 2 for odd and even and >> to the number of bits in i/2 
        return arr
