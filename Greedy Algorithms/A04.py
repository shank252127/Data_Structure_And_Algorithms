class Solution:
	
    def mice(self, A, B):
        A.sort()
        B.sort()
        diff=[]
        for i in range(len(A)):
            b=B[i]
            a=A[i]			
            d = a-b
            d = abs(d)
            diff.append(d)
        return max(diff)

a = Solution()
ans = a.mice( [ -10, -79, -79, 67, 93, -85, -28, -94 ], [ -2, 9, 69, 25, -31, 23, 50, 78 ])
print(ans)
