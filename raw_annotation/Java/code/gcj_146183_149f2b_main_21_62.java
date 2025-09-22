import java.util.*;
public class Solution {
    private static Scanner sc;
    private static class Temp implements Comparable<Temp>{
        int idx;
        long score;
        Temp(int idx, long score) {
            this.idx = idx;
            this.score = score;
        }
        @Override
        public int compareTo(Temp o) {
            if (this.score < o.score) {
                return -1;
            } else if (this.score > o.score) {
                return 1;
            }
            return 0;
        }
    }
    public static void main(String[] args) {
        sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int test = 1; test <= T; ++test) {
            int n = sc.nextInt();
            long[][] A = new long [n][2];
            Set<List<Integer>> S = new HashSet<>();
            Set<Long> S3 = new HashSet<>();
            S3.add(1L);
            for (int i = 0; i < n; ++i) {
                A[i][0] = sc.nextLong();
                A[i][1] = sc.nextLong();
                S3.add(A[i][0]);
                S3.add(A[i][1]);
            }
            for (long a : S3) {
                for (long b : S3) {
                    for (long c = 1 ; c <= 2 ; ++ c) {
                        for (long d = 1; d <= 2; ++ d) {
                            List<Temp> B = new ArrayList<>();
                            List<Integer> C = new ArrayList<>();
                            Set<Long> S2 = new HashSet<>();
                            for (int i = 0; i < n; ++i) {
                                B.add(new Temp(i, A[i][0] * a * c + A[i][1] * b * d));
                                S2.add(A[i][0] * a * c + A[i][1] * b * d);
                            }
                            if (S2.size() != n) {
                                continue;
                            }
                            Collections.sort(B);
                            for (Temp temp : B) {
                                C.add(temp.idx);
                            }
                            S.add(C);
                        }
                    }
                }
            }
            System.out.println("Case #" + test + ": " + S.size());
        }
        sc.close();
    }
}