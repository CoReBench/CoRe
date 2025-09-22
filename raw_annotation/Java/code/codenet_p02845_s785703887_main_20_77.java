import java.io.BufferedReader;
import java.io.Closeable;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Map.Entry;
import java.util.PriorityQueue;
import java.util.Random;
import java.util.StringTokenizer;
import java.util.TreeSet;
public class Main {
	public static void main(String[] args) throws IOException {	
		try(final Scanner sc = new Scanner(System.in)){
			final int N = sc.nextInt();
			final long MOD = 1000000007;
			int fst = -1, snd = -1, thd = -1;
			long answer = 1;
			for(int i = 0; i < N; i++) {
				final int val = sc.nextInt();
				if(val == 0) {
					if(fst == -1) 
						{ fst = 1; }
					else if(snd == -1) 
						{ snd = 1; }
					else if(thd == -1) 
						{ thd = 1; }
				}else {
					if(fst == val && snd == val && thd == val) {
						fst += 1; 
						answer *= 3; 
						answer %= MOD;
					}else if(fst == val && snd == val) {
						fst += 1; 
						answer *= 2; 
						answer %= MOD;
					}else if(snd == val && thd == val) {
						snd += 1; 
						answer *= 2; 
						answer %= MOD;
					}else if(thd == val && fst == val) {
						fst += 1; 
						answer *= 2; 
						answer %= MOD;
					}else if(fst == val) {
						fst += 1;
					}else if(snd == val) {
						snd += 1;
					}else if(thd == val) {
						thd += 1;
					}
					int old_fst = fst, old_snd = snd, old_thd = thd;
					fst = Math.max(old_fst, Math.max(old_snd, old_thd));
					thd = Math.min(old_fst, Math.min(old_snd, old_thd));
					snd = (old_fst + old_snd + old_thd) - fst - thd; 
				}
			}
			if(snd < 0 && thd < 0) {
				answer *= 3; 
				answer %= MOD;
			}else if(thd < 0) {
				answer *= 6; 
				answer %= MOD;
			}else {
				answer *= 6; 
				answer %= MOD;
			}
			System.out.println(answer);
		}
	}
	public static class Scanner implements Closeable {
		private BufferedReader br;
		private StringTokenizer tok;
		public Scanner(InputStream is) throws IOException {
			br = new BufferedReader(new InputStreamReader(is));
		}
		private void getLine() throws IOException {
			while(!hasNext()){
				tok = new StringTokenizer(br.readLine());
			}
		}
		private boolean hasNext() {
			return tok != null && tok.hasMoreTokens();
		}
		public String next() throws IOException {
			getLine();
			return tok.nextToken();
		}
		public int nextInt() throws IOException {
			return Integer.parseInt(next());
		}
		public long nextLong() throws IOException {
			return Long.parseLong(next());
		}
		public double nextDouble() throws IOException {
			return Double.parseDouble(next());
		}
		public int[] nextIntArray(int n) throws IOException {
			final int[] ret = new int[n];
			for(int i = 0; i < n; i++){
				ret[i] = this.nextInt();
			}
			return ret;
		}
		public long[] nextLongArray(int n) throws IOException {
			final long[] ret = new long[n];
			for(int i = 0; i < n; i++){
				ret[i] = this.nextLong();
			}
			return ret;
		}
		public void close() throws IOException {
			br.close();
		}
	}
}