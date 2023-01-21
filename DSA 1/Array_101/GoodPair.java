
import java.util.Arrays;

// Solution 1; TC - O(n^2); SC - O(1);
class Solution {
    public int solve(int[] A, int B) {
        for (int i = 0; i < A.length; i++) {
            for (int j = i + 1; j < A.length; j++) {
                if (A[i] + A[j] == B) {
                    return 1;
                }
            }
        }
        return 0;
    }
}

// Solution 2; TC = O(nlogn); SC - O(1);
class Solution02 {
    public int solve(int[] A, int B) {
        Arrays.sort(A);
        int a = 0;
        int b = A.length - 1;
        while (a < b) {
            if (A[a] + A[b] == B) {
                return 1;
            } else if (A[a] + A[b] > B) {
                b = b - 1;

            } else {
                a = a + 1;
            }
        }
        return 0;
    }
}

class GoodPair {
    public static void main(String args[]) {
        // Solution 1 :
        Solution sol = new Solution();
        int[] a = { 1, 2, 3, 4 };
        int b = 7;
        int result = sol.solve(a, b);
        System.out.println(result);
        // Solution 2 :
        Solution02 sol2 = new Solution02();
        System.out.println(sol2.solve(a, b));
    }
}
