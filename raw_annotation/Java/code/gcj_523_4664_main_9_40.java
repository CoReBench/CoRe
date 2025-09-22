import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;
public class Solution {
    private static long guessNumber(long lowerBound, long upperBound) {
        if (lowerBound == upperBound) return lowerBound;
        return (upperBound - lowerBound) / 2 + lowerBound;
    }
    public static void main(String[] args) {
        private static final String TOO_BIG = "TOO_BIG";
        private static final String TOO_SMALL = "TOO_SMALL";
        private static final String CORRECT = "CORRECT";
        private static final String WRONG_ANSWER = "WRONG_ANSWER";
        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int t = Integer.parseInt(in.nextLine());
        for (int i = 1; i <= t; ++i) {
            String[] splits = in.nextLine().split(" ");
            long a = Long.parseLong(splits[0]) + 1;
            long b = Long.parseLong(splits[1]);
            int n = Integer.parseInt(in.nextLine());
            while (n-- > 0) {
                long cur;
                if (a == b)
                    cur = a;
                else
                    cur = (b - a) / 2 + a;
                System.out.println(cur);
                String result = in.nextLine().trim();
                if (TOO_BIG.equals(result)) {
                    b = cur - 1;
                } else if (TOO_SMALL.equals(result)) {
                    a = cur + 1;
                } else if (CORRECT.equals(result)) {
                    break;
                } else {
                    return;
                }
            }
        }
    }
}