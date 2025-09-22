import java.util.*;
import java.io.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;
import static java.lang.Math.*;
public class Main {
	void run() {
		int INF = 1 << 28;
		double EPS = 1e-10;
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(), t = sc.nextInt(), s = sc.nextInt();
		int[] as = new int[n], bs = new int[n];
		for(int i=0;i<n;i++) {
			as[i] = sc.nextInt(); bs[i] = sc.nextInt();
		}
		int[] dp1 = new int[s+1], dp2 = new int[n+1];
		fill(dp1, -1); dp1[0] = 0;
		for(int i=0;i<n;i++) 
			for(int j=s;j>=0;j--) 
				if(dp1[j] >= 0){
					if(bs[i] + j <= s && dp1[bs[i]+j] < dp1[j] + as[i]) {
						dp1[bs[i]+j] = dp1[j] + as[i];
						dp2[i+1] = max(dp1[bs[i]+j], dp2[i+1]);
					}
				}
		for(int i=1;i<=n;i++) 
			dp2[i] = max(dp2[i], dp2[i-1]);
		int[] dp3 = new int[t-s+1], dp4 = new int[n+1];
		fill(dp3, -1); dp3[0] = 0;
		for(int i=n-1;i>=0;i--) 
			for(int j=t-s;j>=0;j--) 
				if(dp3[j] >= 0) {
					if(bs[i] + j <= t-s && dp3[bs[i]+j] < dp3[j] + as[i]) {
						dp3[bs[i]+j] = dp3[j] + as[i];
						dp4[n-i] = max(dp3[bs[i]+j], dp4[n-i]);
					}
				}
		for(int i=1;i<=n;i++) 
			dp4[i] = max(dp4[i], dp4[i-1]);
		int max = 0;
		for(int i=0;i<n;i++) 
			max = max(max, dp2[i] + dp4[n-i]);
		System.out.println(max);
	}
	void debug(Object... os) {
		System.err.println(Arrays.deepToString(os));
	}
	public static void main(String[] args) {
		new Main().run();
	}
}