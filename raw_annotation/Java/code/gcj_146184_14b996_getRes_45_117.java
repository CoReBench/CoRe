import java.lang.*;
import java.io.*;
import java.util.*;
class Solution {
    public static void main(String[]args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        int T = Integer.parseInt(br.readLine());
        for(int i=1;i<=T;i++) {
            pw.println("Case #" + i + ": " + solve(br));
        }
        pw.flush();
    }
    private static String solve(BufferedReader br) throws IOException {
        int N = Integer.parseInt(br.readLine());
        List<P> paris = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            paris.add(new P(x, y));
        }
        String res = getRes(N, paris);
        return res;
    }
    private static boolean check(String res, List<P> paris) {
        if (res.equals("IMPOSSIBLE")) return true;
        StringTokenizer st = new StringTokenizer(res);
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int[] v = new int[paris.size()];
        for (int i = 0; i < paris.size(); i++) {
            int z = paris.get(i).a * x + paris.get(i).b * y;
            v[i] = z;
        }
        int[] v2 = new int[v.length];
        System.arraycopy(v, 0, v2, 0, v.length);
        Arrays.sort(v);
        boolean r = Arrays.equals(v, v2);
        if (!r) {
            debug(v, v2);
        }
        return r;
    }
    private static String getRes(int n, List<P> paris) {
        TreeSet<F> pfracs = new TreeSet<>();
        TreeSet<F> nfracs = new TreeSet<>();
        boolean hasDup = false;
        for (int i = 0; i < n; i++) {
            P p1 = paris.get(i);
            for (int j = i + 1; j < n; j++) {
                P p2 = paris.get(j);
                int d1 = p1.a - p2.a;
                int d2 = p1.b - p2.b;
                if ((d1 == 0 && d2 == 0) || (d1 > 0 && d2 > 0)) {
                    hasDup = true;
                    break;
                }
                if (d1 != 0 && d2 != 0 && (d1 > 0 || d2 > 0)) {
                    if (d1 < 0) {
                        pfracs.add(new F(Math.abs(d1), Math.abs(d2)));
                    }
                    if (d2 < 0) {
                        nfracs.add(new F(Math.abs(d1), Math.abs(d2)));
                    }
                }
            }
            if (hasDup) break;
        }
        if (hasDup) {
            return "IMPOSSIBLE";
        }
        F above = pfracs.isEmpty() ? null : pfracs.first();
        F below = nfracs.isEmpty() ? null : nfracs.last();
        if (above != null && below != null && above.compareTo(below) <= 0) {
            return "IMPOSSIBLE";
        }
        if (above == null && below == null) {
            return "1 1";
        }
        if (above == null) {
            long z = below.num;
            long r = below.denum;
            long y = 0;
            if (r % z == 0) {
                y = r / z;
            } else {
                y = r / z + 1;
            }
            return "1 " + (y + 1);
        }
        if (below == null) {
            long z = above.num;
            long r = above.denum;
            long x = 0;
            if (r % z == 0) {
                x = r / z;
            } else {
                x = r / z + 1;
            }
            return (x + 1) + " 1";
        }
        int gcd = gcd(above.denum, below.denum);
        long b2 = above.denum / gcd;
        long lcd = below.denum * b2;
        long a = above.num * (lcd / above.denum);
        long b = below.num * (lcd / below.denum);
        long z = a - b;
        long r = 2 * lcd;
        long x = 0;
        if (r % z == 0) {
            x = r / z;
        } else {
            x = r / z + 1;
        }
        return x + " " + (x + 1);
    }
    private static int gcd(int a, int b) {
        return (b != 0) ? gcd(b, a % b) : a;
    }
    private static final class P {
        int a;
        int b;
        public P(int a, int b) {
            this.a = a;
            this.b = b;
        }
    }
    private static final class F implements Comparable<F> {
        int num;
        int denum;
        public F(int num, int denum) {
            int gcd = gcd(num, denum);
            this.num = num / gcd;
            this.denum = denum / gcd;
        }
        @Override
        public int compareTo(F o) {
            int gcd = gcd(o.denum, denum);
            long b2 = o.denum / gcd;
            long lcd = denum * b2;
            long a = num * (lcd / denum);
            long b = o.num * (lcd / o.denum);
            return Long.compare(a, b);
        }
    }
    public static void debug(Object...args) {
        System.out.println(Arrays.deepToString(args));
    }
}