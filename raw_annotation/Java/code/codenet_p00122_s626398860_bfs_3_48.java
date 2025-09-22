import java.util.*;
public class Main {
	public static boolean bfs (int sx,int sy, int[] spx, int[] spy) {
		int size = 10, spCnt = 0;
		int[] dx = {-1,0,1,-1,0,1,-2,-2,-2,2,2,2};
		int[] dy = {-2,-2,-2,2,2,2,-1,0,1,-1,0,1};
		int[] dx2 = {0,0,1,1,1,0,-1,-1,-1};
		int[] dy2 = {0,-1,-1,0,1,1,1,0,-1,-1};
		boolean[][] park = new boolean[size][size];
		Queue<Integer> queueX = new LinkedList<Integer>();
		Queue<Integer> queueY = new LinkedList<Integer>();
		queueX.add(sx);
		queueY.add(sy);
		while (!queueX.isEmpty()) {
			if (spCnt == spx.length) {
				return true;
			}
			for (int i = 0; i < dx2.length; i++) {
				int y = spy[spCnt] + dy2[i];
				int x = spx[spCnt] + dx2[i];
				if (0 <= y && y < size &&
					0 <= x && x < size) {
					park[y][x] = true;
				}
			}
			Queue<Integer> nx = new LinkedList<Integer>();
			Queue<Integer> ny = new LinkedList<Integer>();
			while (!queueX.isEmpty()) {
				int x = queueX.poll();
				int y = queueY.poll();
				for (int i = 0; i < dx.length; i++) {
					int nextX = x + dx[i];
					int nextY = y + dy[i];
					if (0 <= nextX && nextX < 10 &&
						0 <= nextY && nextY < 10 &&
						park[nextY][nextX]) {
						nx.add(nextX);
						ny.add(nextY);
					}
				}
			}
			spCnt++;
			park = new boolean[size][size];
			queueX = nx;
			queueY = ny;
		}
		return false;
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (true) {
			int sx = sc.nextInt();
			int sy = sc.nextInt();
			if (sx == 0 && sy == 0) break;
			sc.nextLine();
			int n = sc.nextInt();
			int[] spx = new int[n];
			int[] spy = new int[n];
			sc.nextLine();
			for (int i = 0; i < n; i++) {
				spx[i] = sc.nextInt();
				spy[i] = sc.nextInt();
			}
			sc.nextLine();
			System.out.println(bfs(sx,sy,spx,spy) ? "OK" : "NA");
		}
	}
}