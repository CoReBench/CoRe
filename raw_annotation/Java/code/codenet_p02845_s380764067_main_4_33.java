import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws Exception {
        long mod = (long)Math.pow(10,9)+7;
        FastScanner sc = new FastScanner(System.in);
        int n = sc.nextInt();
        long[] arr = new long[3];
        long ff = sc.nextLong();
        if(ff != 0){
            System.out.println(0);
            return;
        }
        long ans = 1;
        arr[0] = 1;
        for(int i = 0; i < n-1; i++){
            int fi = -1;
            long cnt = 0;
            long a = sc.nextLong();
            for(int j = 0; j < 3; j++){
                if(arr[j] == a){
                    cnt++;
                    if(fi == -1){
                        arr[j]++;
                        fi = j;
                    }
                }
            }
            ans *= cnt;
            ans %= mod;
        }
        System.out.println((ans*3)%mod);
    }
}
class FastScanner {
    private BufferedReader reader = null;
    private StringTokenizer tokenizer = null;
    public FastScanner(InputStream in) {
        reader = new BufferedReader(new InputStreamReader(in));
        tokenizer = null;
    }
    public String next() {
        if (tokenizer == null || !tokenizer.hasMoreTokens()) {
            try {
                tokenizer = new StringTokenizer(reader.readLine());
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
        return tokenizer.nextToken();
    }
    public String nextLine() {
        if (tokenizer == null || !tokenizer.hasMoreTokens()) {
            try {
                return reader.readLine();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
        return tokenizer.nextToken("\n");
    }
    public long nextLong() {
        return Long.parseLong(next());
    }
    public int nextInt() {
        return Integer.parseInt(next());
    }
    public double nextDouble() {
         return Double.parseDouble(next());
    }
    public int[] nextIntArray(int n) {
        int[] a = new int[n];
        for (int i = 0; i < n; i++)
            a[i] = nextInt();
        return a;
    }
    public long[] nextLongArray(int n) {
        long[] a = new long[n];
        for (int i = 0; i < n; i++)
            a[i] = nextLong();
        return a;
    } 
}