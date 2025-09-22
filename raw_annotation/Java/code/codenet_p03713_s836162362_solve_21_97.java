import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskC solver = new TaskC();
        solver.solve(1, in, out);
        out.close();
    }
    static class TaskC {
        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int h = in.nextInt();
            int w = in.nextInt();
            if (h % 3 == 0 || w % 3 == 0) {
                out.println(0);
                return;
            }
            int offset = 2000;
            int minSum = Integer.MAX_VALUE;
            for (int a = h / 3 - offset; a < h / 3 + offset; a++) {
                if (a <= 0 || a >= h)
                    continue;
                for (int b = w / 2 - offset; b < w / 2 + offset; b++) {
                    if (b <= 0 || b >= w)
                        continue;
                    int s1 = a * w;
                    int s2 = b * (h - a);
                    int s3 = (h - a) * (w - b);
                    int max = Math.max(Math.max(s1, s2), s3);
                    int min = Math.min(Math.min(s1, s2), s3);
                    minSum = Math.min(minSum, max - min);
                }
            }
            int x = h;
            h = w;
            w = x;
            for (int a = h / 3 - offset; a < h / 3 + offset; a++) {
                if (a <= 0 || a >= h)
                    continue;
                for (int b = w / 2 - offset; b < w / 2 + offset; b++) {
                    if (b <= 0 || b >= w)
                        continue;
                    int s1 = a * w;
                    int s2 = b * (h - a);
                    int s3 = (h - a) * (w - b);
                    int max = Math.max(Math.max(s1, s2), s3);
                    int min = Math.min(Math.min(s1, s2), s3);
                    minSum = Math.min(minSum, max - min);
                }
            }
            for (int a = h / 3 - offset; a < h / 3 + offset; a++) {
                if (a <= 0 || a >= h)
                    continue;
                for (int b = h / 3 - offset; b < h / 3 + offset; b++) {
                    if (b <= 0 || b >= h)
                        continue;
                    if (a + b >= h)
                        continue;
                    int s1 = a * w;
                    int s2 = b * w;
                    int s3 = (h - a - b) * w;
                    int max = Math.max(Math.max(s1, s2), s3);
                    int min = Math.min(Math.min(s1, s2), s3);
                    minSum = Math.min(minSum, max - min);
                }
            }
            x = h;
            h = w;
            w = x;
            for (int a = h / 3 - offset; a < h / 3 + offset; a++) {
                if (a <= 0 || a >= h)
                    continue;
                for (int b = h / 3 - offset; b < h / 3 + offset; b++) {
                    if (b <= 0 || b >= h)
                        continue;
                    if (a + b >= h)
                        continue;
                    int s1 = a * w;
                    int s2 = b * w;
                    int s3 = (h - a - b) * w;
                    int max = Math.max(Math.max(s1, s2), s3);
                    int min = Math.min(Math.min(s1, s2), s3);
                    minSum = Math.min(minSum, max - min);
                }
            }
            out.println(minSum);
        }
    }
    static class InputReader {
        StringTokenizer st;
        BufferedReader br;
        public InputReader(InputStream is) {
            BufferedReader br = new BufferedReader(new InputStreamReader(is));
            this.br = br;
        }
        public String next() {
            if (st == null || !st.hasMoreTokens()) {
                String nextLine = null;
                try {
                    nextLine = br.readLine();
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
                if (nextLine == null)
                    return null;
                st = new StringTokenizer(nextLine);
            }
            return st.nextToken();
        }
        public int nextInt() {
            return Integer.parseInt(next());
        }
    }
}