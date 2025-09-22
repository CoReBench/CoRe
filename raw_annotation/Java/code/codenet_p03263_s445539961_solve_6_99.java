import java.io.*;
import java.util.*;
public class Main {
	private static Scanner sc;
	private static Printer pr;
	private static void solve() {
		int h = sc.nextInt();
		int w = sc.nextInt();
		int[][] a = new int[h][w];
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				a[i][j] = sc.nextInt();
			}
		}
		List<Integer> x = new ArrayList<>();
		List<Integer> y = new ArrayList<>();
		boolean flag = false;
		int prex = 0;
		int prey = 0;
		boolean odd;
		for (int i = 0; i < h; i++) {
			if (i % 2 == 1) {
				for (int j = w - 1; j >= 0; j--) {
					if (a[i][j] % 2 == 1) {
						odd = true;
					} else {
						odd = false;
					}
					if (odd && flag) {
						flag = !flag;
						x.add(prex);
						y.add(prey);
						x.add(j);
						y.add(i);
						prex = j;
						prey = i;
					} else if (odd && !flag) {
						flag = !flag;
						prex = j;
						prey = i;
					} else if (!odd && flag) {
						x.add(prex);
						y.add(prey);
						x.add(j);
						y.add(i);
						prex = j;
						prey = i;
					} else if (!odd && !flag) {
					}
				}
			} else {
				for (int j = 0; j < w; j++) {
					if (a[i][j] % 2 == 1) {
						odd = true;
					} else {
						odd = false;
					}
					if (odd && flag) {
						flag = !flag;
						x.add(prex);
						y.add(prey);
						x.add(j);
						y.add(i);
						prex = j;
						prey = i;
					} else if (odd && !flag) {
						flag = !flag;
						prex = j;
						prey = i;
					} else if (!odd && flag) {
						x.add(prex);
						y.add(prey);
						x.add(j);
						y.add(i);
						prex = j;
						prey = i;
					} else if (!odd && !flag) {
					}
				}
			}
		}
		pr.println(x.size() / 2);
		for (int i = 0, size = x.size(); i < size / 2 * 2; i++) {
			if (i % 2 == 0) {
				StringBuilder sb = new StringBuilder();
				sb.append(y.get(i) + 1);
				sb.append(' ');
				sb.append(x.get(i) + 1);
				sb.append(' ');
				pr.print(sb.toString());
			} else {
				StringBuilder sb = new StringBuilder();
				sb.append(y.get(i) + 1);
				sb.append(' ');
				sb.append(x.get(i) + 1);
				pr.println(sb.toString());
			}
		}
	}
	public static void main(String[] args) {
		sc = new Scanner(System.in);
		pr = new Printer(System.out);
		solve();
		pr.close();
		sc.close();
	}
	static class Scanner {
		BufferedReader br;
		Scanner (InputStream in) {
			br = new BufferedReader(new InputStreamReader(in));
		}
		private boolean isPrintable(int ch) {
			return ch >= '!' && ch <= '~';
		}
		private boolean isCRLF(int ch) {
			return ch == '\n' || ch == '\r' || ch == -1;
		}
		private int nextPrintable() {
			try {
				int ch;
				while (!isPrintable(ch = br.read())) {
					if (ch == -1) {
						throw new NoSuchElementException();
					}
				}
				return ch;
			} catch (IOException e) {
				throw new NoSuchElementException();
			}
		}
		String next() {
			try {
				int ch = nextPrintable();
				StringBuilder sb = new StringBuilder();
				do {
					sb.appendCodePoint(ch);
				} while (isPrintable(ch = br.read()));
				return sb.toString();
			} catch (IOException e) {
				throw new NoSuchElementException();
			}
		}
		int nextInt() {
			try {
				boolean negative = false;
				int res = 0;
				int limit = -Integer.MAX_VALUE;
				int radix = 10;
				int fc = nextPrintable();
				if (fc < '0') {
					if (fc == '-') {
						negative = true;
						limit = Integer.MIN_VALUE;
					} else if (fc != '+') {
						throw new NumberFormatException();
					}
					fc = br.read();
				}
				int multmin = limit / radix;
				int ch = fc;
				do {
					int digit = ch - '0';
					if (digit < 0 || digit >= radix) {
						throw new NumberFormatException();
					}
					if (res < multmin) {
						throw new NumberFormatException();
					}
					res *= radix;
					if (res < limit + digit) {
						throw new NumberFormatException();
					}
					res -= digit;
				} while (isPrintable(ch = br.read()));
				return negative ? res : -res;
			} catch (IOException e) {
				throw new NoSuchElementException();
			}
		}
		long nextLong() {
			try {
				boolean negative = false;
				long res = 0;
				long limit = -Long.MAX_VALUE;
				int radix = 10;
				int fc = nextPrintable();
				if (fc < '0') {
					if (fc == '-') {
						negative = true;
						limit = Long.MIN_VALUE;
					} else if (fc != '+') {
						throw new NumberFormatException();
					}
					fc = br.read();
				}
				long multmin = limit / radix;
				int ch = fc;
				do {
					int digit = ch - '0';
					if (digit < 0 || digit >= radix) {
						throw new NumberFormatException();
					}
					if (res < multmin) {
						throw new NumberFormatException();
					}
					res *= radix;
					if (res < limit + digit) {
						throw new NumberFormatException();
					}
					res -= digit;
				} while (isPrintable(ch = br.read()));
				return negative ? res : -res;
			} catch (IOException e) {
				throw new NoSuchElementException();
			}
		}
		float nextFloat() {
			return Float.parseFloat(next());
		}
		double nextDouble() {
			return Double.parseDouble(next());
		}
		String nextLine() {
			try {
				int ch;
				while (isCRLF(ch = br.read())) {
					if (ch == -1) {
						throw new NoSuchElementException();
					}
				}
				StringBuilder sb = new StringBuilder();
				do {
					sb.appendCodePoint(ch);
				} while (!isCRLF(ch = br.read()));
				return sb.toString();
			} catch (IOException e) {
				throw new NoSuchElementException();
			}
		}
		void close() {
			try {
				br.close();
			} catch (IOException e) {
			}
		}
	}
	static class Printer extends PrintWriter {
		Printer(OutputStream out) {
			super(out);
		}
	}
}