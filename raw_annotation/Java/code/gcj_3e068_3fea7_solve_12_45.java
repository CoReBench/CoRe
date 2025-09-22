import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;
public class Solution {
	public static void main(String[] args) {
		solve();
	}
	private static void solve() {
		Scanner sc = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		long t = sc.nextLong();
		sc.nextLine();
		for (long i2 = 0; i2 < t; i2++) {
			int n = sc.nextInt();
			boolean sold[] = new boolean[n];
			for (int i = 0; i < n; i++) {
				int d = sc.nextInt();
				int p[] = new int[d];
				ArrayList<Integer> wants = new ArrayList<Integer>();
				for (int j = 0; j < d; j++) {
					int x = sc.nextInt();
					p[j] = x;
					if (!sold[x-1]) {
						wants.add(x);
					}
				}
				if (d == 0) {
					System.out.println(-1);
				} else {
					if (wants.size() == 0) {
						System.out.println(-1);
					} else {
						int idx = (int) Math.floor(wants.size()*Math.random());
						int toSell = wants.get(idx);
						sold[toSell-1] = true;
						System.out.println(toSell);
					}
				}
			}
		}
		sc.close();
	}
}