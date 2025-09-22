import java.awt.*;
import java.awt.geom.*;
import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
public class Solution {
	private static BufferedReader br;
	private static StringTokenizer st;
	private static PrintWriter pw;
	public static void main(String[] args) throws Exception {
		br = new BufferedReader(new InputStreamReader(System.in));
		pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
		int qq = readInt();
		for(int casenum = 1; casenum <= qq; casenum++) {
			pw.print("Case #" + casenum + ": ");
			int r = readInt();
			int c = readInt();
			int ret = 1;
			char[][] g = new char[r][c];
			for(int i = 0; i < r; i++) {
				String s = nextToken();
				for(int j = 0; j < c; j++) {
					g[i][j] = s.charAt(j);
				}
			}
			for(int mask = 1; mask < (1<<(r*c)); mask++) {
				if(Integer.bitCount(mask) <= ret) 
					continue;
				int t = mask;
				par = new int[r*c];
				for(int i = 0; i < r*c; i++) {
					par[i] = i;
				}
				boolean[][] use = new boolean[r][c];
				for(int i = 0; i < r; i++) {
					for(int j = 0; j < c; j++) {
						if((t&1) != 0) {
							use[i][j] = true;
						}
						t >>= 1;
					}
				}
				int numNeed = Integer.bitCount(mask)-1;
				for(int i = 0; i < r; i++) {
					for(int j = 0; j < c; j++) {
						if(!use[i][j]) 
							continue;
						if(i+1 < r && use[i+1][j] && merge(i*c+j, (i+1)*c+j)) {
							numNeed--;
						}
						if(j+1 < c && use[i][j+1] && merge(i*c+j, i*c+j+1)) {
							numNeed--;
						}
					}
				}
				if(numNeed != 0) 
					continue;
				boolean valid = false;
				for(int i = 0; !valid && i < r; i++) {
					for(int j = 0; !valid && j < c; j++) {
						Set<Character>[] all = new Set[4];
						for(int a = 0; a < 4; a++) {
							all[a] = new HashSet<Character>();
						}
						boolean good = true;
						for(int x = 0; good && x < r; x++) {
							for(int y = 0; good && y < c; y++) {
								if(!use[x][y]) 
									continue;
								int idx = 0;
								if(x > i) 
									idx |= 2;
								if(y < j) 
									idx |= 1;
								all[idx].add(g[x][y]);
								if (all[idx].size() < 2)
									good = true;
								else
									good = false;
							}
						}
						valid = good;
					}
				}
				if(!valid) 
					continue;
				ret = Integer.bitCount(mask);
			}
			pw.println(ret);
		}
		pw.close();
	}
	static int[] par;
	public static int find(int x) {
		return par[x] == x ? x : (par[x] = find(par[x]));
	}
	public static boolean merge(int x, int y) {
		int fx = find(x);
		int fy = find(y);
		if(fx == fy) 
			return false;
		par[fx] = fy;
		return true;
	}
	private static void exitImmediately() {
		pw.close();
		System.exit(0);
	}
	private static long readLong() throws IOException {
		return Long.parseLong(nextToken());
	}
	private static double readDouble() throws IOException {
		return Double.parseDouble(nextToken());
	}
	private static int readInt() throws IOException {
		return Integer.parseInt(nextToken());
	}
	private static String nextLine() throws IOException  {
		String s = br.readLine();
		if(s == null) {
			exitImmediately();
		}
		st = null;
		return s;
	}
	private static String nextToken() throws IOException  {
		while(st == null || !st.hasMoreTokens())  {
			st = new StringTokenizer(nextLine().trim());
		}
		return st.nextToken();
	}
}