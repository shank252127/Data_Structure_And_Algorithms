from heapq import heapify, heappush, heappop


class Solution:
    def solve(self, A, B):
        obj = []
        maxDeadline = max(A)

        # creating a list of object = {"end" : val, "start" : val };
        for i in range(len(A)):
            obj.append({"profit": B[i], "deadline": A[i]})

        # sorting list of object on the basis of the key = "deadline";
        a = sorted(obj, key=lambda x: x['deadline'])

        # Creating empty heap
        heap = []
        heapify(heap)
        currentTime = 0

        for i in a:
            if len(heap) < maxDeadline:
                currentTime = currentTime + 1
                if(currentTime <= i["deadline"]):
                    # Adding items to the heap using heappush function
                    heappush(heap, i["profit"])
                else:
                    smallest = heappop(heap)
                    if(smallest < i["profit"]):
                        heappush(heap, i["profit"])
                    else:
                        heappush(heap, smallest)
                    # decreasing current time when one of the value is replaced
                    currentTime = currentTime - 1
            # when length of heap == highest deadline
            elif len(heap) == maxDeadline and currentTime <= i["deadline"]:
                smallest = heappop(heap)
                if(smallest < i["profit"]):
                    heappush(heap, i["profit"])
                else:
                    heappush(heap, smallest)

        # returning answer in mod as asked;
        return sum(list(heap)) % 1000000007


a = Solution()
ans = a.solve([1, 7, 6, 2, 8, 4, 4, 6, 8, 2], [8, 11, 7, 7, 10, 8, 7, 5, 4, 9])
print(ans)
