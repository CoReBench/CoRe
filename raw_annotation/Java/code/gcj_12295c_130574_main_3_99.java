import java.util.*;
public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for (int i = 1; i <= t; i++) {
			int p = sc.nextInt();
			int q = sc.nextInt();
			ArrayList<Person> ppl = new ArrayList<Person>(p);
			for (int j = 0; j < p; j++) {
				int b = sc.nextInt(); 
				int a = q - sc.nextInt() - 1;
				String c = sc.next();
				int d = 0;
				int e = 0;
				if (c.equals("N")) {
					e = -1;
				}
				else if (c.equals("S")) {
					e = 1;
				}
				else if (c.equals("E")) {
					d = 1;
				}
				else {
					d = -1;
				}
				ppl.add(new Person(a, b, d, e));
			}
			int[][] b = new int[q][q];
			for (Person a : ppl) {
				int x = a.x;
				int y = a.y;
				if (a.xDir == 0) {
					for (int j = x+a.yDir; j < q && j >= 0; j += a.yDir) {
						for (int k = 0; k < q; k++) {
							b[j][k]++;
						}
					}
				} else {
					for (int j = 0; j < q; j++) {
						for (int k = y+a.xDir; k < q && k >= 0; k += a.xDir) {
							b[j][k]++;
						}
					}
				}
			}
			int max = 0;
			for (int j = 0; j < q; j++) {
				for (int k = 0; k < q; k++) {
					if (b[j][k] > max)
						max = b[j][k];
				}
			}
			int row[] = new int[q*q];
			int col[] = new int[q*q];
			int num = 0;
			for (int c = 0; c < q; c++) {
				for (int r = 0; r < q; r++) {
					if (b[r][c] == max) {
						row[num] = q - r - 1;
						col[num] = c;
						num++;
					}
				}
			}
			int min = Integer.MAX_VALUE;
			ArrayList<Person> f = new ArrayList<Person>(q*q);
			for(int j = 0; j < num; j++) {
				if(row[j] + col[j] < min) {
					min = row[j] + col[j];
					f.clear();
					f.add(new Person(row[j],col[j],0,0));
				}
				else if(row[j] + col[j] == min) {
					f.add(new Person(row[j],col[j],0,0));
				}
			}
			ArrayList<Person> g = new ArrayList<Person>(f.size());
			int m = Integer.MAX_VALUE;
			for(int j = 0; j < f.size(); j++) {
				if(m > f.get(j).x) {
					m = f.get(j).x;
					g.clear();
					g.add(f.get(j));
				}
				else if(m == f.get(j).x) {
					g.add(f.get(j));
				}
			}
			Person z = g.get(0);
			for(int j = 1; j < g.size(); j++) {
				if(g.get(j).y < z.y) {
					z = g.get(j);
				}
			}
			System.out.println("Case #" + i + ": " + z.y + " " + z.x);
		}
	}
	public static class Person {
		int x;
		int y;
		int xDir;
		int yDir;
		public Person(int a, int b, int c, int d) {
			x = a;
			y = b;
			xDir = c;
			yDir = d;
		}
	}
}