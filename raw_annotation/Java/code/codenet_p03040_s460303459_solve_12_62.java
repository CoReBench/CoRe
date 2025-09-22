import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Collections;
import java.util.InputMismatchException;
import java.util.NoSuchElementException;
import java.util.PriorityQueue;
public class Main {
	static PrintWriter out;
	static InputReader ir;
	static void solve() {
		int Q = ir.nextInt();
		PriorityQueue<Long> f = new PriorityQueue<>(Collections.reverseOrder());
		PriorityQueue<Long> l = new PriorityQueue<>();
		long fsum = 0, lsum = 0;
		long B = 0;
		while (Q-- > 0) {
			int com = ir.nextInt();
			if (com == 1) {
				long a = ir.nextLong();
				if (f.size() == l.size()) {
					if (l.size() == 0) {
						f.add(a);
						fsum += a;
					} else {
						long x = l.peek();
						if (x < a) {
							lsum += a - x;
							fsum += x;
							l.poll();
							l.add(a);
							f.add(x);
						} else {
							fsum += a;
							f.add(a);
						}
					}
				} else {
					long x = f.peek();
					if (x <= a) {
						lsum += a;
						l.add(a);
					} else {
						lsum += x;
						fsum += a - x;
						f.poll();
						f.add(a);
						l.add(x);
					}
				}
				B += ir.nextLong();
			} else {
				long x = f.peek();
				if (f.size() == l.size()) {
					out.println(x + " " + (lsum - fsum + B));
				} else {
					out.println(x + " " + (lsum - fsum + x + B));
				}
			}
		}
	}
	public static void main(String[] args) {
		ir = new InputReader(System.in);
		out = new PrintWriter(System.out);
		solve();
		out.flush();
	}
	static class InputReader {
		private InputStream in;
		private byte[] buffer = new byte[1024];
		private int curbuf;
		private int lenbuf;
		public InputReader(InputStream in) {
			this.in = in;
			this.curbuf = this.lenbuf = 0;
		}
		public boolean hasNextByte() {
			if (curbuf >= lenbuf) {
				curbuf = 0;
				try {
					lenbuf = in.read(buffer);
				} catch (IOException e) {
					throw new InputMismatchException();
				}
				if (lenbuf <= 0)
					return false;
			}
			return true;
		}
		private int readByte() {
			if (hasNextByte())
				return buffer[curbuf++];
			else
				return -1;
		}
		private boolean isSpaceChar(int c) {
			return !(c >= 33 && c <= 126);
		}
		private void skip() {
			while (hasNextByte() && isSpaceChar(buffer[curbuf]))
				curbuf++;
		}
		public boolean hasNext() {
			skip();
			return hasNextByte();
		}
		public String next() {
			if (!hasNext())
				throw new NoSuchElementException();
			StringBuilder sb = new StringBuilder();
			int b = readByte();
			while (!isSpaceChar(b)) {
				sb.appendCodePoint(b);
				b = readByte();
			}
			return sb.toString();
		}
		public int nextInt() {
			if (!hasNext())
				throw new NoSuchElementException();
			int c = readByte();
			while (isSpaceChar(c))
				c = readByte();
			boolean minus = false;
			if (c == '-') {
				minus = true;
				c = readByte();
			}
			int res = 0;
			do {
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res = res * 10 + c - '0';
				c = readByte();
			} while (!isSpaceChar(c));
			return (minus) ? -res : res;
		}
		public long nextLong() {
			if (!hasNext())
				throw new NoSuchElementException();
			int c = readByte();
			while (isSpaceChar(c))
				c = readByte();
			boolean minus = false;
			if (c == '-') {
				minus = true;
				c = readByte();
			}
			long res = 0;
			do {
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res = res * 10 + c - '0';
				c = readByte();
			} while (!isSpaceChar(c));
			return (minus) ? -res : res;
		}
		public double nextDouble() {
			return Double.parseDouble(next());
		}
		public int[] nextIntArray(int n) {
			int[] a = new int[n];
			for (int i = 0; i < n; i++)
				a[i] = nextInt();
			return a;
		}
		public long[] nextLongArray(int n) {
			long[] a = new long[n];
			for (int i = 0; i < n; i++)
				a[i] = nextLong();
			return a;
		}
		public char[][] nextCharMap(int n, int m) {
			char[][] map = new char[n][m];
			for (int i = 0; i < n; i++)
				map[i] = next().toCharArray();
			return map;
		}
	}
	static void tr(Object... o) {
		out.println(Arrays.deepToString(o));
		out.flush();
	}
}