class Solution:
	# @param A : list of integers
	# @return an integer
    def candy(self, A):
        arr=A;
        candy=[]
        for i in range(len(A)):
            candy.append(1)
        candy[0]=1
        
        for i in range(1,len(A)):
            if(A[i]>A[i-1] and candy[i]<=candy[i-1]):
                candy[i]=candy[i-1]+1;
        
        for i in range(len(A)-2,-1,-1):
            if(A[i]>A[i+1] and candy[i]<=candy[i+1]):
                candy[i]=candy[i+1]+1;

        s=0
        for i in candy:
            s=s+i;
        return s

            

        
        

a=Solution();

ans= a.candy([1,5,2,1])
print(ans)
            

        