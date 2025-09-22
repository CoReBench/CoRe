import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
public class Solution {
	private static void solve(Scanner in) {
		for(int i = 1; i <= 17; ++i) {
			in.next();
			System.out.println( i + " 100" );
		}
		for(int i = 1; i <= 68; ++i) {
			in.next();
			System.out.println( ((i % 17) + 1) + " " + i );
			System.out.flush();
		}
		String [] res = new String[3];
		int[] num = new int[3];
		int m = 1000;
		int ind = 0;
		for(int i = 0; i < 3; ++i) {
			in.next();
			System.out.println( (18 + i) + " 0");
			int n = in.nextInt();
			int p = 1;
			for(int k = 0; k < n; ++k) {
				int t = in.nextInt();
				if (t == p) {
					p++;
				}
			}
			if (n < m) {
				m = n;
				ind = i;
			}
			num[i] = p;
		}
		for (int i = 0; i < 4; ++i) {
			for(int j = 0; j < 3; ++j) {
				if (j != ind) {
					in.next();
					System.out.println( 18 + j + " " + num[j] );
				}
			}
		}
		in.next();
		System.out.println( "19 0" );
		int n = in.nextInt();
		for(int i = 0; i < n; ++i) {
			in.next();
		}
		for(int i = 18; i <= 20; ++i) {
			in.next();
			System.out.println( i + " 100" );
		}
		System.out.flush();
	}
	public static void main(String[] args) {
		Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		int t = in.nextInt(); 
		for (int i = 1; i <= t; ++i) {
			solve(in);
		}
	}
}