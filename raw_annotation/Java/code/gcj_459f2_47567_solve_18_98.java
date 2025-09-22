import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for (int i = 0; i < t; i++) {
			solve(sc, i + 1);
		}
	}
	static Map<Integer, Set<Integer>> all;
	static int l;
	private static void solve(Scanner sc, int num) {
		boolean result = false;
		int c = sc.nextInt();
		int[] b = new int[c];
		int[] r = new int[c];
		for (int i = 0; i < c; i++) {
			b[i] = sc.nextInt();
			r[i] = 1;
		}
		int[] d = new int[c];
		List<String> l = new ArrayList<>();
		boolean good = false;
		String s = "";
		while (true) {
			result = true;
			for (int i = 0; i < c; i++) {
				if (b[i] != r[i]) {
					result = false;
				}
			}
			if (result) {
				break;
			}
			int cl = 0;
			int last = 0;
			int[] z = new int[c];
			 good = false;
			  s = "";
			  int[] rr = new int[c];
			for (int i = 0; i < c; i++) {
				if (b[i] > 0) {
					int want = b[i];
					int nexttmp = 0;
					for (int j = last; j < c ; j++) {
						nexttmp = 0;
						if (r[j] == 0) {
							s += ".";
							continue;
						}
						want-=r[j];
						if (j > i && j > 0&& j  < c-1) {
							z[j] = -1;
							rr[j-1] += r[j];
							good = true;
							s += "/";
						} else 
						if (j < i && j > 0&& j  < c-1) {
							z[j] = 1;
							rr[j+1]+= r[j];
							good = true;
							s += "\\";
						} else {
							s += ".";
							rr[j]+=r[j];
						}
						if (want <= 0) {
							last = j+1;
							break;
						}
					}
				}
			}
			r = rr;
			l.add(s);
			if (!good)
			break;
		}
		if (!result) {
			System.out.println("Case #" + num + ": IMPOSSIBLE");
		} else {
			s = "";
			for (int i = 0; i < c ; i++) {
				s+=".";
			}
			l.add(s);
			System.out.println("Case #" + num + ": " + l.size());
			for (String string : l) {
				System.out.println(string);
			}
		}
	}
	private static String find(Node root, int h) {
		if (h == l) {
			return null;
		}
		if (root.map.size() < all.get(h).size()) {
			for (Integer ii : all.get(h)) {
				if (root.map.get(ii) == null) {
					char rr = (char) ('A' + ii);
					return Character.toString(rr);
				}
			}
		} else {
			for (Map.Entry<Integer, Node> node : root.map.entrySet()) {
				String res = find(node.getValue(), h + 1);
				if (res != null) {
					char rr = (char) ('A' + node.getKey());
					return Character.toString(rr) + res;
				}
			}
		}
		return null;
	}
}
class Node {
	public Map<Integer, Node> map = new HashMap<>();
}