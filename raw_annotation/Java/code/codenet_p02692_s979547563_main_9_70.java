import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
public class Main {
    public static void main(final String[] args) {
        final FastScanner scanner = new FastScanner(System.in);
        final int n = scanner.nextInt();
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();
        final List<String> answer = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            final String s = scanner.next();
            switch (s) {
                case "AB": {
                    if (a == 0 && b == 0) {
                        System.out.println("No");
                        return;
                    }
                    if (a < b) {
                        answer.add("A");
                        a++;
                        b--;
                    } else {
                        answer.add("B");
                        a--;
                        b++;
                    }
                    break;
                }
                case "BC": {
                    if (b == 0 && c == 0) {
                        System.out.println("No");
                        return;
                    }
                    if (b < c) {
                        answer.add("B");
                        b++;
                        c--;
                    } else {
                        answer.add("C");
                        b--;
                        c++;
                    }
                    break;
                }
                default: {
                    if (a == 0 && c == 0) {
                        System.out.println("No");
                        return;
                    }
                    if (a < c) {
                        answer.add("A");
                        a++;
                        c--;
                    } else {
                        answer.add("C");
                        a--;
                        c++;
                    }
                }
            }
        }
        System.out.println("Yes");
        answer.forEach(System.out::println);
    }
    private static class FastScanner {
        private final BufferedReader reader;
        private StringTokenizer tokenizer;
        FastScanner(final InputStream in) {
            reader = new BufferedReader(new InputStreamReader(in));
        }
        String next() {
            if (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (final IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }
        int nextInt() {
            return Integer.parseInt(next());
        }
        long nextLong() {
            return Long.parseLong(next());
        }
        double nextDouble() {
            return Double.parseDouble(next());
        }
        String nextLine() {
            if (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    return reader.readLine();
                } catch (final IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken("\n");
        }
    }
}