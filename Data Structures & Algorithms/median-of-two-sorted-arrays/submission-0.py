class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            A, B, = B, A

        l, r = 0, len(A) - 1
        while True:
            i = l + (r - l) // 2
            j = half - i - 2
            
            Aleft = A[i] if i >= 0 else -sys.maxsize
            Aright = A[i + 1] if (i + 1) < len(A) else sys.maxsize

            Bleft = B[j] if j >= 0 else -sys.maxsize
            Bright = B[j + 1] if (j + 1) < len(B) else sys.maxsize

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
        
        return -1
        


'''
ex1:
1, 2, 3, 4, 5

6, 7, 8, 9


ex2:
6, 7, 8, 9, 10

1, 2, 3, 4


ex3:
1, 3, 6, 8

2, 4, 5, 9


ex4:
2, 5, 6, 7

1, 2, 3, 4, 5
'''