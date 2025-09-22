import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.List;
import java.util.Scanner;
import java.util.ArrayList;
public class Solution {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        Task solver = new Task();
        solver.solve(1, in, out);
        out.close();
    }
    static class Task {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            int T = in.nextInt();
            for (int t = 1; t <= T; t++) {
                int N, B, F;
                N = in.nextInt();
                B = in.nextInt();
                F = in.nextInt();
                List<String> reply = new ArrayList<>();
                for (int i = 0; i < F; i++) {
                    int k = 1 << i;
                    for (int j = 0; j < N; j++) {
                        if ((j & k) == 0) {
                            out.print(0);
                        } else {
                            out.print(1);
                        }
                    }
                    out.println();
                    out.flush();
                    reply.add(in.next());
                }
                int p = 0;
                boolean first = true;
                int i;
                for (i = 0; i < N && p + B < N; i++) {
                    StringBuilder sb = new StringBuilder();
                    for (int j = F - 1; j >= 0; j--) {
                        sb.append(reply.get(j).charAt(p));
                    }
                    int val = Integer.parseInt(sb.toString(), 2);
                    if (val != i) {
                        for (; i < val; i++) {
                            if (!first) {
                                out.print(" ");
                            }
                            first = false;
                            out.print(i);
                        }
                    }
                    p++;
                }
                for (; i < N; i++) {
                    if (!first) {
                        out.print(" ");
                    }
                    first = false;
                    out.print(i);
                }
                out.println();
                out.flush();
                if (in.nextInt() == -1) {
                    return;
                }
            }
        }
    }
}