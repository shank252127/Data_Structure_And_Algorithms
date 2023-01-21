// TC - O(N); SC - O(N);
class Solution {
    public String[] fizzBuzz(int A) {
        String[] res = new String[A];
        for (int i = 0; i < A; i++) {
            if ((i + 1) % 3 == 0 && (i + 1) % 5 == 0) {
                res[i] = "FizzBuzz";
            } else if ((i + 1) % 3 == 0) {
                res[i] = "Fizz";
            } else if ((i + 1) % 5 == 0) {
                res[i] = "Buzz";
            } else {
                res[i] = String.valueOf(i + 1);
                ;
            }
        }
        return res;
    }
}

public class FizzBuzz {
    public static void main(String args[]) {
        Solution sol = new Solution();
        System.out.println(sol.fizzBuzz(5));
    }
}