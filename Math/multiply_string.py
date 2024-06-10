class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # converting both numbers into int 
        num1 = num1[::-1]
        num2 = num2[::-1]
        result = [0] * (len(num1)+len(num2))
        for i, digit1 in enumerate(num1):
            for j, digit2 in enumerate(num2):
                result[i+j] += int(digit1)*int(digit2)
                result[i+j+1] += result[i+j]//10
                result[i+j] %= 10
        result = result[::-1]
        #removing the resulting zeros
        
        start =0
        while start < len(result) and result[start] == 0:
            start+=1

        return ''.join(map(str, result[start:])) or '0'
