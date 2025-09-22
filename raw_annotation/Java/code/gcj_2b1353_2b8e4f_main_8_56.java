import java.io.BufferedReader;
import java.io.Closeable;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
class Solution {
	public static void main(String[] args){
		try(Scanner sc = new Scanner(System.in)){
			final int T = sc.nextInt();
			LOOP:
			for(int tt = 0; tt < T; tt++){
				final int N = sc.nextInt();
				System.out.printf("Case #%d:\n", tt + 1);
				System.out.printf("%d %d\n", 1, 1);
				long rest = N - 1;
				long depth = 1;
				long position = 0;
				while(true) {
					final long lines = depth + 1;
					final long line_sum = 1l << depth;
					if(rest < line_sum) {
						break;
					}
					if(line_sum * 2 < rest) {
						System.out.printf("%d %d\n", depth + 1, position + 1);
						rest -= 1;
					}else {
						if(position == 0) {
							for(long i = 0; i < lines; i++) {
								System.out.printf("%d %d\n", depth + 1, i + 1);
							}
							position = lines;
						}else {
							for(long i = position; i >= 0; i--) {
								System.out.printf("%d %d\n", depth + 1, i + 1);
							}
							position = 0;
						}
						rest -= line_sum;
					}
					depth++;
 				}
				while(rest > 0) {
					if(position == 0) {
						System.out.printf("%d %d\n", depth + 1, position + 1);
					}else {
						System.out.printf("%d %d\n", depth + 1, position + 1);
						position++;
					}
					rest--;
					depth++;
				}
			}
		}
	}
	public static class Scanner implements Closeable {
		private BufferedReader br;
		private StringTokenizer tok;
		public Scanner(InputStream is) {
			br = new BufferedReader(new InputStreamReader(is));
		}
		private void getLine() {
			try {
				while (!hasNext()) {
					tok = new StringTokenizer(br.readLine());
				}
			} catch (IOException e) { 
			}
		}
		private boolean hasNext() {
			return tok != null && tok.hasMoreTokens();
		}
		public String next() {
			getLine();
			return tok.nextToken();
		}
		public int nextInt() {
			return Integer.parseInt(next());
		}
		public long nextLong() {
			return Long.parseLong(next());
		}
		public double nextDouble() {
			return Double.parseDouble(next());
		}
		public void close() {
			try {
				br.close();
			} catch (IOException e) { 
			}
		}
	}
}