import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.InputMismatchException;
import java.io.IOException;
import java.io.InputStream;
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        FastScanner in = new FastScanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        FStringsOfEternity solver = new FStringsOfEternity();
        solver.solve(1, in, out);
        out.close();
    }
    static class FStringsOfEternity {
        public void solve(int testNumber, FastScanner br, PrintWriter pw) {
            String in1 = br.nextString();
            String in2 = br.nextString();
            char[] t = in1.toCharArray();
            char[] s = in2.toCharArray();
            if (t.length > s.length) {
                int orig = 0;
                boolean poss = true;
                for (int i = 0; i < t.length - s.length; i += s.length) {
                    if (!in1.substring(i, i + s.length).equals(in2)) {
                        poss = false;
                    } else {
                        orig++;
                    }
                }
                if (poss) {
                    pw.println(-1);
                    pw.close();
                }
                int ans = 0;
                for (int i = 0; i < t.length - s.length; i += s.length) {
                    if (in1.substring(i, i + s.length).equals(in2)) {
                        ans++;
                    } else {
                        break;
                    }
                }
                for (int i = t.length - s.length; i >= 0; i -= s.length) {
                    if (in1.substring(i, i + s.length).equals(in2)) {
                        ans++;
                    } else {
                        break;
                    }
                }
                pw.println(Math.max(orig, ans));
                pw.close();
            } else if (s.length == t.length) {
                if (s.equals(t)) {
                    pw.println(-1);
                } else {
                    pw.println(0);
                }
            } else {
                int orig = 0;
                boolean poss = true;
                for (int i = 0; i < s.length - t.length; i += s.length) {
                    if (!in2.substring(i, i + t.length).equals(in1)) {
                        poss = false;
                    }
                }
                if (poss) {
                    pw.println(-1);
                    pw.close();
                }
                int ans = 0;
                for (int i = 0; i < s.length - t.length; i += t.length) {
                    if (in2.substring(i, i + t.length).equals(in1)) {
                        ans++;
                    } else {
                        break;
                    }
                }
                for (int i = s.length - t.length; i >= 0; i -= t.length) {
                    if (in2.substring(i, i + t.length).equals(in1)) {
                        ans++;
                    } else {
                        break;
                    }
                }
                pw.println(Math.max(orig, ans));
                pw.close();
            }
        }
    }
    static class FastScanner {
        private InputStream stream;
        private byte[] buf = new byte[1024];
        private int curChar;
        private int numChars;
        private FastScanner.SpaceCharFilter filter;
        public FastScanner(InputStream stream) {
            this.stream = stream;
        }
        public int read() {
            if (numChars == -1) {
                throw new InputMismatchException();
            }
            if (curChar >= numChars) {
                curChar = 0;
                try {
                    numChars = stream.read(buf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (numChars <= 0) {
                    return -1;
                }
            }
            return buf[curChar++];
        }
        public String nextString() {
            int c = read();
            while (isSpaceChar(c)) {
                c = read();
            }
            StringBuilder res = new StringBuilder();
            do {
                if (Character.isValidCodePoint(c)) {
                    res.appendCodePoint(c);
                }
                c = read();
            } while (!isSpaceChar(c));
            return res.toString();
        }
        public boolean isSpaceChar(int c) {
            if (filter != null) {
                return filter.isSpaceChar(c);
            }
            return isWhitespace(c);
        }
        public static boolean isWhitespace(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }
        public interface SpaceCharFilter {
            public boolean isSpaceChar(int ch);
        }
    }
}