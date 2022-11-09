class Solution:
    def solve(self, A, B):
        obj = []

        # creating a list of object = {"end" : val, "start" : val };
        for i in range(len(A)):
            obj.append({"end": B[i], "start": A[i]})

        # sorting list of object on the basis of the key = "end";
        a = sorted(obj, key=lambda x: x['end'])

        # finding the mximum number of job that can be done;
        cnt = 0
        end = 0
        for i in range(len(a)):
            if i == 0:
                cnt = cnt + 1
                end = a[i]["end"]
                continue

            if a[i]["start"] >= end:
                cnt = cnt + 1
                end = a[i]["end"]
                
        return cnt


a = Solution()

ans = a.solve(  [ 3, 13, 7, 7, 10, 3 ], [ 6, 15, 9, 8, 16, 11 ])
print(ans)
