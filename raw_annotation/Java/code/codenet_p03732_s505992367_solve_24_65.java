import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.IOException;
import java.util.InputMismatchException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.util.Collections;
import java.io.InputStream;
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskD solver = new TaskD();
        solver.solve(1, in, out);
        out.close();
    }
    static class TaskD {
        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int n = in.nextInt();
            long W = in.nextLong();
            ArrayList<Long>[] lists = new ArrayList[4];
            for (int i = 0; i < 4; i++) {
                lists[i] = new ArrayList<>();
            }
            long w1 = in.nextLong();
            long v1 = in.nextLong();
            lists[0].add(v1);
            for (int i = 1; i < n; i++) {
                long w = in.nextLong();
                long v = in.nextLong();
                lists[(int) (w - w1)].add(v);
            }
            for (int i = 0; i < 4; i++) {
                lists[i].sort(Collections.reverseOrder());
            }
            long[][] sum = new long[4][];
            for (int i = 0; i < 4; i++) {
                int m = lists[i].size();
                sum[i] = new long[m + 1];
                for (int j = 0; j < m; j++) {
                    sum[i][j + 1] = lists[i].get(j);
                }
                for (int j = 0; j < m; j++) {
                    sum[i][j + 1] += sum[i][j];
                }
            }
            long ans = 0;
            for (int i = 0; i <= lists[0].size(); i++) {
                for (int j = 0; j <= lists[1].size(); j++) {
                    for (int k = 0; k <= lists[2].size(); k++) {
                        for (int l = 0; l <= lists[3].size(); l++) {
                            if (w1 * i + (w1 + 1) * j + (w1 + 2) * k + (w1 + 3) * l > W) continue;
                            ans = Math.max(ans, sum[0][i] + sum[1][j] + sum[2][k] + sum[3][l]);
                        }
                    }
                }
            }
            out.println(ans);
        }
    }
    static class InputReader {
        BufferedReader in;
        StringTokenizer tok;
        public String nextString() {
            while (!tok.hasMoreTokens()) {
                try {
                    tok = new StringTokenizer(in.readLine(), " ");
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
            }
            return tok.nextToken();
        }
        public int nextInt() {
            return Integer.parseInt(nextString());
        }
        public long nextLong() {
            return Long.parseLong(nextString());
        }
        public InputReader(InputStream inputStream) {
            in = new BufferedReader(new InputStreamReader(inputStream));
            tok = new StringTokenizer("");
        }
    }
}