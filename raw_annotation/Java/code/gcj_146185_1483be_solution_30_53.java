import java.util.Scanner;
import java.util.*;
public class Solution{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int t = input.nextInt();
        for(int t_0=0;t_0<t;t_0++) {
            int numOfElem = input.nextInt();
            Map<Integer, List<Integer>> graph = new HashMap<>();
            for(int i = 0;i<numOfElem;i++){
                int x = input.nextInt()-1;
                int y = input.nextInt()-1;
                if(!graph.containsKey(x)) {
                    graph.put(x, new LinkedList<>());
                }
                if(!graph.containsKey(y)) {
                    graph.put(y, new LinkedList<>());
                }
                graph.get(x).add(i);
                graph.get(y).add(i);
            }
            int[] startElem = new int[numOfElem];
            for(int i=0;i<numOfElem;i++) {
                startElem[i] = input.nextInt();
            }
            int solution = !graph.containsKey(0)?startElem[0]:solution(graph, numOfElem, startElem);
            System.out.println("Case #" + (t_0+1) + ": " + (solution==-1?"UNBOUNDED":solution));
        }
    }
    private static int solution(Map<Integer, List<Integer>> graph, int numOfElem, int[] startElem) {
            Set<Integer> visited = new HashSet<>();
            visited.add(0);
            Queue<Integer> q = new LinkedList<>();
            int result = startElem[0];
            for(int i: graph.get(0)) {
                if(i != 0)
                    q.add(i);
            }
            boolean acyclic = false;
            while(!q.isEmpty()) {
                int next = q.poll();
                for(int neighbor: graph.get(next)) {
                    if(visited.contains(neighbor)) {
                        acyclic = true;
                    } else {
                        result += startElem[neighbor];
                        q.add(neighbor);
                        visited.add(neighbor);
                    }
                }
            }
            return acyclic?(result==0?0:-1):result;
    }
}