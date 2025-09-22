import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(input.readLine());
        for (int i = 1; i <= T; i++) {
            System.out.println("Case #" + i + ": " + solve(input));
        }
    }
    private static String solve(BufferedReader input) throws IOException {
        int M = Integer.parseInt(input.readLine());
        int[] part1 = new int[M];
        int[] part2 = new int[M];
        int[] quantities = new int[M];
        for (int i=0; i<M; i++) {
            String[] nums = input.readLine().split(" ");
            part1[i] = Integer.parseInt(nums[0])-1;
            part2[i] = Integer.parseInt(nums[1])-1;
        }
        String[] nums = input.readLine().split(" ");
        for(int i=0; i<M; i++) {
            quantities[i] = Integer.parseInt(nums[i]);
        }
        Map<Integer, Integer> transmuted = new HashMap<Integer, Integer>();
        transmuted.put(part1[0], 1);
        transmuted.put(part2[0], 1);
        boolean stuck = false;
        while(!stuck) {
            int min = Integer.MAX_VALUE;
            for (Map.Entry<Integer, Integer> pair : transmuted.entrySet()) {
                if (quantities[pair.getKey()] / pair.getValue() < min) 
                    min = quantities[pair.getKey()] / pair.getValue();
            }
            quantities[0] += min;
            for (Map.Entry<Integer, Integer> pair : transmuted.entrySet()) {
                quantities[pair.getKey()] -= min * pair.getValue();
            }
            Map<Integer, Integer> newTransmuted = new HashMap<Integer, Integer>();
            for (Map.Entry<Integer, Integer> pair : transmuted.entrySet()) {
                int metal = pair.getKey();
                int quantity = pair.getValue();
                if (pair.getValue() > quantities[metal]) {
                    if (part1[metal] == 0 || part2[metal] == 0 || pair.getValue() > 1000*1000*1000) {
                        stuck = true;
                        break;
                    } else {
                        if (newTransmuted.containsKey(part1[metal])) {
                            newTransmuted.put(part1[metal], newTransmuted.get(part1[metal]) + quantity);
                        } else {
                            newTransmuted.put(part1[metal], quantity);
                        }
                        quantities[part1[metal]] += quantities[metal];
                        if (newTransmuted.containsKey(part2[metal])) {
                            newTransmuted.put(part2[metal], newTransmuted.get(part2[metal]) + quantity);
                        } else {
                            newTransmuted.put(part2[metal], quantity);
                        }
                        quantities[part2[metal]] += quantities[metal];
                        if (newTransmuted.containsKey(metal)) {
                            newTransmuted.put(metal, newTransmuted.get(metal) - quantity);
                        } else {
                            newTransmuted.put(metal, -1*quantity);
                        }
                        quantities[metal] = 0;
                    }
                }
            }
            for (Map.Entry<Integer, Integer> pair : newTransmuted.entrySet()) {
                Integer metal = pair.getKey();
                Integer quantity = pair.getValue();
                if (transmuted.containsKey(metal)) {
                    transmuted.put(metal, transmuted.get(metal) + quantity);
                }
                else {
                    transmuted.put(metal, quantity);
                }
                if (transmuted.get(metal) == 0) {
                    transmuted.remove(metal);
                }
            }
        }
        return String.valueOf(quantities[0]);
    }
}