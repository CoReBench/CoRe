import java.util.*;
public class Solution {
  public static void main(String args[]) {
    (new Solution()).solve();
  }
  void solve() {
    Scanner cin = new Scanner(System.in);
    int T = cin.nextInt();
    for(int C=1; C<=T; ++C) {
    	long N = cin.nextLong();
    	long K = cin.nextLong();
    	PriorityQueue<Long> queue = new PriorityQueue<Long>();
    	Map<Long, Long> count = new HashMap<Long, Long>();
    	queue.add(-N);
    	count.put(N, 1L);
    	long ans = 0;
    	while( true ) {
    		long cur = -queue.poll();
    		long rest = count.get(cur);
    		if( K <= 1 ) {
    			ans = cur;
    			break;
    		}
    		K -= rest;
    		if( K <= 0 ) {
    			ans = cur;
    			break;
    		}
    		long large = cur / 2;
    		long small = (cur - 1) / 2;
    		if( count.containsKey(large) ) {
    			count.put(large, count.get(large) + rest);
    		}
    		else {
    			queue.add(-large);
    			count.put(large, rest);
    		}
    		if( count.containsKey(small) ) {
    			count.put(small, count.get(small) + rest);
    		}
    		else {
    			queue.add(-small);
    			count.put(small, rest);
    		}
    	}
      System.out.println("Case #" + C + ": " + (ans / 2) + " " + ((ans - 1) / 2));
    }
    cin.close();
  }
}