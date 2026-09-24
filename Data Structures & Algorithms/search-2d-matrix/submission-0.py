class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       m=len(matrix) # number of rows
       n=len(matrix[0]) #number of cols
       for row in matrix:
        s=0
        e= len(row)-1
        while s<=e:
            mid=s+(e-s)//2
            if target==row[mid]:
                return True
            elif target<row[mid]:
                e=mid-1
            else: 
                s=mid+1
       return False