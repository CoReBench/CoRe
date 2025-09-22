import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        solve(in);
    }
    public static void solve(Scanner in){
        int T = in.nextInt();
        int F = in.nextInt();
        for (int t = 1; t <= T; ++t) {
            System.out.println(solveSingle(in));
            char r = in.next();
        }
    }
    static String solveSingle(Scanner in) {
        StringBuilder sol = new StringBuilder();
        List<Character> chars = new ArrayList<>();
        chars.add('A');
        chars.add('B');
        chars.add('C');
        chars.add('D');
        chars.add('E');
        Map<Character, ArrayList<Integer>> occ5 = new HashMap<>();
        for (char c : chars) {
            occ5.put(c, new ArrayList<>());
        }
        for (int i = 0; i < 119; i++) {
            int c = i * 5 + 1;
            System.out.println(c);
            char n = in.next().charAt(0);
            List<Integer> curr = occ5.get(n);
            curr.add(c);
        }
        for (Map.Entry<Character, ArrayList<Integer>> e5 : occ5.entrySet()) {
            if (e5.getValue().size() != 24) {
                sol.append(e5.getKey());
                chars.remove(e5.getKey());
                Map<Character, ArrayList<Integer>> occ4 = new HashMap<>();
                for (char c : chars) {
                    occ4.put(c, new ArrayList<>());
                }
                for (int i = 0; i < 23; i++) {
                    int c = i * 5 + 2;
                    System.out.println(c);
                    char n = in.next().charAt(0);
                    List<Integer> curr = occ4.get(n);
                    curr.add(c);
                }
                for (Map.Entry<Character, ArrayList<Integer>> e4 : occ4.entrySet()) {
                    if (e4.getValue().size() != 6) {
                        sol.append(e4.getKey());
                        chars.remove(e4.getKey());
                        Map<Character, ArrayList<Integer>> occ3 = new HashMap<>();
                        for (char c : chars) {
                            occ3.put(c, new ArrayList<>());
                        }
                        for (int i = 0; i < 5; i++) {
                            int c = i * 5 + 3;
                            System.out.println(c);
                            char n = in.next().charAt(0);
                            List<Integer> curr = occ3.get(n);
                            curr.add(c);
                        }
                        for (Map.Entry<Character, ArrayList<Integer>> e : occ3.entrySet()) {
                            if (e.getValue().size() != 2) {
                                chars.remove(e.getKey());
                                sol.append(e.getKey());
                                int askLast = e.getValue().get(0) + 1;
                                System.out.println(askLast);
                                char n = in.next().charAt(0);
                                for (char c : chars) {
                                    if (c != n) {
                                        sol.append(c);
                                        break;
                                    }
                                }
                                sol.append(n);
                            }
                        }
                    }
                }
            }
        }
        return sol.toString();
    }
    public static int toInt(char c) {
        return c;
    }
}