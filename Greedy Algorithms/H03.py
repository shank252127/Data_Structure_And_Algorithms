from heapq import heappop, heappush, heapify
class Solution:
   
    def solve(self, A, B, C):
        # Creating empty heap
        heap = []
        heapify(heap)
        for i in C:
            heappush(heap, i)

        maxVal = 0
        minVal = 0 
        arrMax = C
        arrMax.sort()
        for i in range(A):
            #handling max value
            a = arrMax.pop()
            #inserting the value a-1 again into the list if it's > 1;
            if( a-1 >0):
                arrMax.append(a-1)
            maxVal = maxVal + a
            arrMax.sort()
            #handling min value
            m=heappop(heap)
            #inserting the value m-1 again into the heap if it's > 1;
            if(m-1>0):
                heappush(heap, m-1)
            minVal = minVal + m

        return [maxVal,minVal]



a = Solution()
ans = a.solve(4,3,[2,1,1])
print(ans)
