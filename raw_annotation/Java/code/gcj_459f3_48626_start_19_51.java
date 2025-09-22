import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import static java.util.Arrays.*;
public class ProblemB2 {
    BufferedReader rd;
    ProblemB2() throws IOException {
        rd = new BufferedReader(new InputStreamReader(System.in));
        compute();
    }
    private void compute() throws IOException {
        start();
        int n = pint();
        for(int i=1;i<=n;i++) {
            out("Case #" + i + ": " + solve());
        }
    }
    int[][] v = new int[123][123];
    private void start() {
        for(int[] q: v) {
            fill(q, -1);
        }
        int[][] rb = new int[111][2];
        int p = 0;
        for(int i=1;i<=6;i++) {
            for(int r=0;r<=i;r++) {
                rb[p][0] = r;
                rb[p][1] = i-r;
                p++;
            }
        }
        int s = 1<<p;
        for(int i=0;i<s;i++) {
            int u = i;
            int r = 0;
            int b = 0;
            int cnt = 0;
            for(int k=0;k<p;k++) {
                if((u&1) > 0) {
                    r += rb[k][0];
                    b += rb[k][1];
                    cnt++;
                }
                u >>= 1;
            }
            int cur = v[r][b];
            if(cur == -1 || (cur < cnt)) {
                v[r][b] = cnt;
            }
        }
    }
    private int solve() throws IOException {
        int[] a = intarr();
        int r = a[0];
        int b = a[1];
        if(v[r][b] != -1) {
            return v[r][b];
        }
        if(r < b) {
            int t = r;
            r = b;
            b = t;
        }
        int res = 0;
        int nxt = 7;
        while(v[r][b] == -1) {
            r -= nxt;
            nxt++;
            res++;
        }
        res += v[r][b];
        return res;
    }
    private int pint() throws IOException {
        return pint(rd.readLine());
    }
    private int pint(String s) {
        return Integer.parseInt(s);
    }
    private int[] intarr() throws IOException {
        return intarr(rd.readLine());
    }
    private int[] intarr(String s) {
        String[] q = split(s);
        int n = q.length;
        int[] a = new int[n];
        for(int i=0;i<n;i++) {
            a[i] = Integer.parseInt(q[i]);
        }
        return a;
    }
    private String[] split(String s) {
        if(s == null) {
            return new String[0];
        }
        int n = s.length();
        int start = -1;
        int end = 0;
        int sp = 0;
        boolean lastWhitespace = true;
        for(int i=0;i<n;i++) {
            char c = s.charAt(i);
            if(isWhitespace(c)) {
                lastWhitespace = true;
            } else {
                if(lastWhitespace) {
                    sp++;
                }
                if(start == -1) {
                    start = i;
                }
                end = i;
                lastWhitespace = false;
            }
        }
        if(start == -1) {
            return new String[0];
        }
        String[] res = new String[sp];
        int last = start;
        int x = 0;
        lastWhitespace = true;
        for(int i=start;i<=end;i++) {
            char c = s.charAt(i);
            boolean w = isWhitespace(c);
            if(w && !lastWhitespace) {
                res[x++] = s.substring(last,i);
            } else if(!w && lastWhitespace) {
                last = i;
            }
            lastWhitespace = w;
        }
        res[x] = s.substring(last,end+1);
        return res;
    }
    private boolean isWhitespace(char c) {
        return c==' ' || c=='\t';
    }
    private static void out(Object x) {
        System.out.println(x);
    }
    public static void main(String[] args) throws IOException {
        new ProblemB2();
    }
}