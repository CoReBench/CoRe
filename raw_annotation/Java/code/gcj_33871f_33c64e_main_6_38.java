import java.io.*;
import java.util.*;
public class Solution{
    StringBuilder sb = new StringBuilder();
    int off = -1000000000;
    public static void main(String[] args) {
        MyScanner sc = new MyScanner();
        out = new PrintWriter(new BufferedOutputStream(System.out));
        long MOD = 1000000007;
        int t = sc.nextInt();
        int tt = 0;
        Solution sol = new Solution();
        while(tt++ < t)
        {
            out.print("Case #" + tt + ": ");
            int C = sc.nextInt(), D = sc.nextInt();
            HashMap <Integer, ArrayList<Integer>> map = new HashMap<>();
            int order[] = new int[C + 1];
            int time[] = new int[C + 1];
            int [][] edges = new int[D][2];
            int [] res = new int[D];
            for(int i = 2; i <= C; i++) {
                order[i] = -sc.nextInt();
                if(map.get(order[i]) == null)
                    map.put(order[i], new ArrayList());
                map.get(order[i]).add(i);
            }
            for(int i = 0; i < D; i++)
            {
                int u = sc.nextInt();
                int v = sc.nextInt();
                res[i] = Math.max(1, Math.abs(order[u] - order[v]));
                out.print(res[i] + " ");
            }
            out.println();
        }
        out.close();
    }
    public int solve(MyScanner sc){
        int res = 0;
        return res;
    }
    public static PrintWriter out;
    public static class MyScanner {
        BufferedReader br;
        StringTokenizer st;
        public MyScanner() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        int nextInt() {
            return Integer.parseInt(next());
        }
        long nextLong() {
            return Long.parseLong(next());
        }
        double nextDouble() {
            return Double.parseDouble(next());
        }
        String nextLine(){
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}