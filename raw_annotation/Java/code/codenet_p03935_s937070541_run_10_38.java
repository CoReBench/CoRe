import java.util.Arrays;
import java.util.Scanner;
public class Main {
    Scanner   sc2   = new Scanner(System.in);
    long      start = System.currentTimeMillis();
    long      fin   = System.currentTimeMillis();
    final int MOD   = 1000000007;
    int[]     dx    = { 1, 0, 0, -1 };
    int[]     dy    = { 0, 1, -1, 0 };
    void run() {
        MyScanner sc    = new MyScanner();
        int n = sc.nextInt();
        int m = sc.nextInt();
        int M = 998244353;
        if (m > 200000) {
            return;
        }
        int[][] dp = new int[2][m];
        int[] sum = new int[m];
        dp[0][0] = 1;
        dp[0][1] = 1;
        sum[0] = 1;
        sum[1] = 2;
        for (int i = 2; i < m; i++) {
            dp[0][i] = (dp[0][i - 1] + dp[0][i - 2]) % M;
            sum[i] = (sum[i - 1] + dp[0][i]) % M;
        }
        long last = dp[0][m - 1];
        for (int i = 1; i < n; i++) {
            int[] next = new int[m];
            next[0] = sum[0];
            for (int j = 1; j < m; j++) 
                next[j] = (next[j - 1] + sum[j]) % M;
            last = sum[m - 1];
            sum = next;
        }
        System.out.println(last);
    }
    public static void main(String[] args) {
        new Main().run();
    }
    void debug(Object... o) {
        System.out.println(Arrays.deepToString(o));
    }
    void debug2(int[][] array) {
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                System.out.print(array[i][j]);
            }
            System.out.println();
        }
    }
    boolean inner(int h, int w, int limH, int limW) {
        return 0 <= h && h < limH && 0 <= w && w < limW;
    }
    void swap(int[] x, int a, int b) {
        int tmp = x[a];
        x[a] = x[b];
        x[b] = tmp;
    }
    int lower_bound(int a[], int k) {
        int l = -1;
        int r = a.length;
        while (r - l > 1) {
            int mid = (l + r) / 2;
            if (k <= a[mid])
                r = mid;
            else
                l = mid;
        }
        return r;
    }
    int upper_bound(int a[], int k) {
        int l = -1;
        int r = a.length;
        while (r - l > 1) {
            int mid = (l + r) / 2;
            if (k < a[mid])
                r = mid;
            else
                l = mid;
        }
        return r;
    }
    long gcd(long a, long b) {
        return a % b == 0 ? b : gcd(b, a % b);
    }
    long lcm(long a, long b) {
        return a * b / gcd(a, b);
    }
    boolean palindrome(String s) {
        for (int i = 0; i < s.length() / 2; i++) {
            if (s.charAt(i) != s.charAt(s.length() - 1 - i)) {
                return false;
            }
        }
        return true;
    }
    class MyScanner {
        int nextInt() {
            try {
                int c = System.in.read();
                while (c != '-' && (c < '0' || '9' < c))
                    c = System.in.read();
                if (c == '-')
                    return -nextInt();
                int res = 0;
                do {
                    res *= 10;
                    res += c - '0';
                    c = System.in.read();
                } while ('0' <= c && c <= '9');
                return res;
            } catch (Exception e) {
                return -1;
            }
        }
        double nextDouble() {
            return Double.parseDouble(next());
        }
        long nextLong() {
            return Long.parseLong(next());
        }
        String next() {
            try {
                StringBuilder res = new StringBuilder("");
                int c = System.in.read();
                while (Character.isWhitespace(c))
                    c = System.in.read();
                do {
                    res.append((char) c);
                } while (!Character.isWhitespace(c = System.in.read()));
                return res.toString();
            } catch (Exception e) {
                return null;
            }
        }
        int[] nextIntArray(int n) {
            int[] in = new int[n];
            for (int i = 0; i < n; i++) {
                in[i] = nextInt();
            }
            return in;
        }
        int[][] nextInt2dArray(int n, int m) {
            int[][] in = new int[n][m];
            for (int i = 0; i < n; i++) {
                in[i] = nextIntArray(m);
            }
            return in;
        }
        double[] nextDoubleArray(int n) {
            double[] in = new double[n];
            for (int i = 0; i < n; i++) {
                in[i] = nextDouble();
            }
            return in;
        }
        long[] nextLongArray(int n) {
            long[] in = new long[n];
            for (int i = 0; i < n; i++) {
                in[i] = nextLong();
            }
            return in;
        }
        char[][] nextCharField(int n, int m) {
            char[][] in = new char[n][m];
            for (int i = 0; i < n; i++) {
                String s = sc.next();
                for (int j = 0; j < m; j++) {
                    in[i][j] = s.charAt(j);
                }
            }
            return in;
        }
    }
}