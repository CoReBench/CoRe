import java.io.*;
import java.util.*;
public class Main {
    static int N;
    static int[] t;
    static int[] v;
    static int[] maxv;
    public static void main(String[] args) throws IOException {
        int totalt = 0;
        MyScanner sc = new MyScanner(System.in);
        int n = sc.nextInt();
        t = new int[n];
        v = new int[n];
        for (int i = 0; i < n; i++) {
            t[i] = sc.nextInt();
            totalt += t[i];
        }
        for (int i = 0; i < n; i++) {
            v[i] = sc.nextInt();
        }
        maxv = new int[totalt + 1];
        int[] ctr = new int[totalt + 1];
        Arrays.fill(maxv, -1);
        maxv[0] = 0;
        maxv[totalt] = 0;
        int tidx = n - 1;
        int mov = 0;
        for (int i = totalt - 1; i > 0; i--) {
            mov++;
            maxv[i] = Math.min(maxv[i + 1] + 1, v[tidx]);
            ctr[i] = v[tidx];
            if (mov == t[tidx]){
                mov = 0;
                tidx--;
            }
        }
        long size = 0;
        long btt = 0;
        int prevHei = 0;
        int ttt = 0;
        int curHei = 0;
        int prepre = 0;
        int perform = 0; 
        for (int i = 1; i < totalt + 1; i++) {
            int mv = maxv[i];
            switch (perform){
                case 0:
                    if (mv >= curHei + 1){
                        curHei++;
                        ttt++;
                    } else {
                        size += (curHei + prevHei) * ttt;
                        prevHei = curHei;
                        ttt = 0;
                        if (mv == curHei){
                            if (maxv[i + 1] == curHei - 1 && ctr[i + 1] > curHei){
                                btt += 1;
                            }
                            perform = 1;
                        } else {
                            perform = 2;
                        }
                        prepre = 0;
                        i--;
                    }
                    break;
                case 1:
                    if (mv == curHei){
                        ttt++;
                    } else {
                        size += curHei * ttt * 2;
                        ttt = 0;
                        prevHei = curHei;
                        if (mv > curHei){
                            perform = 0;
                            size += curHei * 2;
                            i++;
                        } else {
                            perform = 2;
                            if (prepre == 0){
                            }
                        }
                        i--;
                    }
                    break;
                case 2:
                    if (mv == curHei - 1){
                        curHei--;
                        ttt++;
                    } else {
                        size += (prevHei + curHei) * ttt;
                        prevHei = curHei;
                        ttt = 0;
                        if (mv == curHei){
                            perform = 1;
                        } else {
                            perform = 0;
                        }
                        i--;
                    }
                    prepre = 2;
                    break;
            }
        }
        size += (prevHei + curHei) * ttt;
        System.out.println((size+0.0)/ 2 + (btt+0.0)/4);
    }
    static class MyScanner {
        StringTokenizer st;
        BufferedReader br;
        public MyScanner(InputStream s){  br = new BufferedReader(new InputStreamReader(s));}
        public MyScanner(FileReader s) throws FileNotFoundException {br = new BufferedReader(s);}
        public String next() throws IOException
        {
            while (st == null || !st.hasMoreTokens())
                st = new StringTokenizer(br.readLine());
            return st.nextToken();
        }
        public int nextInt() throws IOException {return Integer.parseInt(next());}
        public long nextLong() throws IOException {return Long.parseLong(next());}
        public String nextLine() throws IOException {return br.readLine();}
        public double nextDouble() throws IOException { return Double.parseDouble(next()); }
        public boolean ready() throws IOException {return br.ready();}
    }
}