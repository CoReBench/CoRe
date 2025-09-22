import java.util.LinkedList;
import java.util.Scanner;
public class Solution {
    public static void main(String[] args) {
        String exampleString = "1\n" +
                "12 5\n" +
                "(()(((()))))\n" +
                "1 1 1 1 1 1 1 1 1 1 1 1\n" +
                "1 1 1 1 1 1 1 1 1 1 1 1\n" +
                "1 1 1 1 1 1 1 1 1 1 1 1\n" +
                "7 4 4 12 5\n" +
                "12 11 10 1 6\n";
        Scanner in = new Scanner(System.in);
        int cases = in.nextInt();
        cases:
        for (int i = 1; i <= cases; i++) {
            solve(in, i);
        }
    }
    public static void solve(Scanner in, int caseNumber) {
        int k = in.nextInt();
        int q = in.nextInt();
        String string = in.next();
        int[] linked = buildLinked(string);
        int[][] prices = new int[3][k];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < k; j++) {
                prices[i][j] = in.nextInt();
            }
        }
        int[][] queries = new int[2][q];
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < q; j++) {
                queries[i][j] = in.nextInt();
            }
        }
        int[][] routes = buildRoutes(linked, prices, queries);
        long summ = 0;
        for (int i = 0; i < q; i++) {
            summ += routes[queries[0][i]-1][queries[1][i]-1];
        }
        System.out.printf("Case #%d: %d", caseNumber, summ);
        System.out.println();
    }
    private static int[][] buildRoutes(int[] linked, int[][] prices, int[][] queries) {
        int k = linked.length;
        int[][] routes = new int[k][k];
        for (int i = 0; i < k; i++) {
            for (int j = i-1; j >= 0; j--) {
                routes[i][j] = i == j ? 0 : routes[i][j+1] + prices[0][j];
            }
            for (int j = i; j < k; j++) {
                routes[i][j] = i == j ? 0 : routes[i][j-1] + prices[1][j];
            }
        }
        boolean updated = true;
        while (updated){
            updated = false;
            for (int i = 0; i < k; i++) {
                int pair = linked[i];
                int price = prices[2][i];
                for (int j = 0; j < k; j++) {
                    int newDistance = routes[pair][j] + price;
                    if(newDistance < routes[i][j]){
                        updated = true;
                        routes[i][j] = newDistance;
                    }
                }
            }
        }
        return routes;
    }
    private static int[] buildLinked(String string) {
        int[] linkedPositions = new int[string.length()];
        LinkedList<Integer> integers = new LinkedList<>();
        for (int i = 0; i < string.length(); i++) {
            char current = string.charAt(i);
            if (current == '(') {
                integers.push(i);
            } else {
                Integer pairPosition = integers.poll();
                linkedPositions[pairPosition] = i;
                linkedPositions[i] = pairPosition;
            }
        }
        return linkedPositions;
    }
    private static void printImpossible(int caseNumber) {
        System.out.printf("Case #%d: %s", caseNumber, "IMPOSSIBLE");
        System.out.println();
    }
}