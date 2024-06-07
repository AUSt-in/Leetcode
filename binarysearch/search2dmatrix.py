class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r,c= 0, len(matrix[0])-1
        while r<len(matrix) and c >=0:
            if(matrix[r][c]<target):
                r+=1
            elif(matrix[r][c]>target):
                c-=1
            else:
                return True
        
        return False
