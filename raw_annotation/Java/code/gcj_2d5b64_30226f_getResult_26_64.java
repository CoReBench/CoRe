import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        int numOfCases = Integer.parseInt(input);
        for (int i = 0; i < numOfCases; i++) {
            input = scanner.nextLine();
            TestCase tc = new TestCase(r, s);
            List<String> result = tc.getResult();
            System.out.println("Case #" + (i + 1) + ": " + result.size());
            result.stream().forEach(rs ->
                    System.out.println(rs)
            );
        }
    }
    public static class TestCase {
        int r;
        int s;
        public TestCase(int r, int s) {
            this.r = r;
            this.s = s;
        }
        private List<String> getResult() {
            int r = Integer.parseInt(input.split(" ")[0]);
            int s = Integer.parseInt(input.split(" ")[1]);
            List<String> result = new ArrayList<>();
            List<Integer> v = new ArrayList<>();
            for (int ss = 0; ss < s; ss++) {
                for (int rr = 0; rr < r; rr++) {
                    v.add(rr + 1);
                }
            }
            for (int rr = 0; rr < r - 1; rr++) {
                int current = r - rr;
                int count = s - 1;
                int idx = current * s - 2;
                int start = idx;
                while (count > 0) {
                    boolean found = false;
                    while (!found) {
                        if (v.get(idx) == current) {
                            count--;
                            found = true;
                            int sz = start - idx;
                            result.add(String.format("%d %d", idx + 1, sz));
                            List<Integer> t = new ArrayList<>();
                            while (sz > 0) {
                                sz--;
                                t.add(v.remove(idx + 1));
                            }
                            t.addAll(v);
                            v = t;
                            idx = start;
                            start--;
                        }
                        idx--;
                    }
                }
            }
            return result;
        }
    }
}