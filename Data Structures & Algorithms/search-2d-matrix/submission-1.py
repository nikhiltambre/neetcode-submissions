class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix) # number of rows
        cols=len(matrix[0]) #number of cols
        s=0
        e=rows*cols-1
        while s<=e:
            mid=s+(e-s)//2
            mid_val=matrix[mid//cols][mid%cols]
            if target==mid_val:
                return True
            elif target<mid_val:
                e=mid-1
            else: 
                s=mid+1
        return False