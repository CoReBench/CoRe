import java.util.*;
import java.lang.*;
import java.io.*;
public class Main {
    private static FastScanner sc;
    private static class FastScanner {
        private Scanner sc;
        FastScanner() {
            sc = new Scanner(System.in);
        }
        public int ni() {
            return sc.nextInt();
        }
        public String ns() {
            return sc.nextLine();
        }
        public long nl() {
            return sc.nextLong();
        }
        public double nd() {
            return sc.nextDouble();
        }
    }
    private static void print(Object o) {
        System.out.print(o);
    }
    private static void println(Object o) {
        System.out.println(o);
    }
    private static void printf(String s, Object... data) {
    	System.out.printf(s, data);	
    }
    public static void main(String[] args) {
        sc = new FastScanner();
        solve();
    }
    private static void solve() {
        int N = sc.ni();
        int M = sc.ni();
        long K = sc.nl();
        int[] first = new int[N];
        int[] second = new int[M];
        for(int i = 0; i < N; i++) {
            first[i] = sc.ni();
        }
        for(int i = 0; i < M; i++) {
            second[i] = sc.ni();
        }
        int res = 0;
        int i = 0, j = 0;
        while(i < N && j < M) {
            int val;
            if(first[i] < second[j]) {
                val = first[i];
                i++;
            } else {
                val = second[j];
                j++;
            }
            if(K >= val) {
                K -= val;
                res++;  
            }
        }
        while(i < N) {
            if(K >= first[i]) {
                K -= first[i];
                res++;
            }
            i++;
        }
        while(j < M) {
            if(K >= second[j]) {
                K -= second[j];
                res++;
            } 
            j++;
        }
        println(res);
    }
}