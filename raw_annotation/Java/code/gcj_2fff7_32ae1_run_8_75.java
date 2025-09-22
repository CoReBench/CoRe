import java.util.*;
import java.io.*;
public class Solution {
	public static void main(String[] args) {
		Solution run = new Solution();
		run.run();
	}
	public void run() {
		Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		int numCases = in.nextInt();
		StringBuilder build = new StringBuilder();
		for (int c=1; c<=numCases; c++) {
			build.append(String.format("Case #%d: ",c));
			int n = in.nextInt();
			double p = in.nextInt();
			double[][] dims = new double[n][2];
			double minP = 0;
			for (int i=0; i<n; i++) {
				int first = in.nextInt();
				int second = in.nextInt();
				dims[i][0] = Math.min(first,second);
				dims[i][1] = Math.max(first,second);
				minP += 2 * (first + second);
			}
			boolean small = true;
			smallCheck: for (int i=1; i<n; i++) {
				for (int j=0; j<2; j++) {
					if (dims[i][j] != dims[0][j]) {
						small = false;
						break smallCheck;
					}
				}
			}
			if (minP == p) {
				build.append(String.format("%.7f\n",p));
			}
			else {
				double maxRem = p - minP;
				if (small) {
					int minHalf=0;
					for (; minHalf<n; minHalf++) {
						if (maxRem >= dims[0][0] * 2) {
							maxRem -= dims[0][0] * 2;
						}
						else {
							break;
						}
					}
					if (maxRem == 0) {
						build.append(String.format("%.7f\n",p));
					}
					else {
						int maxHalf=0;
						double maxAdd = Math.sqrt(dims[0][0] * dims[0][0] + dims[0][1] * dims[0][1]) - dims[0][0];
						for (; maxHalf<minHalf; maxHalf++) {
							if (maxRem >= maxAdd * 2) {
								maxRem -= maxAdd * 2;
							}
							else {
								break;
							}
						}
						if (maxHalf < minHalf) {
							maxRem = Math.max(0.0,maxRem - maxAdd * 2);
						}
						build.append(String.format("%.7f\n",p - maxRem));
					}
				}
				else {
					build.append("\n");
				}
			}
		}
		System.out.printf("%s",build);
	}
}