import java.lang.reflect.Array;
import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int T = input.nextInt();
        for (int turn = 0; turn < T; turn++) {
            int n = input.nextInt();
            ArrayList<Point> points = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                Point point = new Point(input.nextLong(),input.nextLong());
                points.add(point);
            }
            ArrayList<Line> lines = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                for (int j = i+1; j < n; j++) {
                    lines.add(new Line(points.get(i),points.get(j)));
                }
            }
            HashMap<Double,ArrayList<Line>> map = new HashMap<>();
            for (int i = 0; i < lines.size(); i++) {
                if (!map.containsKey(lines.get(i).k)) {
                    ArrayList<Line> curr = new ArrayList<>();
                    curr.add(lines.get(i));
                    map.put(lines.get(i).k,curr);
                }else {
                    map.get(lines.get(i).k).add(lines.get(i));
                }
            }
            ArrayList<Integer> results = new ArrayList<>();
            Iterator mapIterator = map.entrySet().iterator();
            while (mapIterator.hasNext()) {
                int result = 0;
                Map.Entry mapElement = (Map.Entry)mapIterator.next();
                HashMap<Double,ArrayList<Line>> bmap = new HashMap<>();
                double k = (double)mapElement.getKey();
                ArrayList<Line> blines = (ArrayList<Line>) mapElement.getValue();
                for (int i = 0; i < blines.size(); i++) {
                    double b = blines.get(i).b;
                    Line l = blines.get(i);
                    if (!bmap.containsKey(b)) {
                        ArrayList<Line> curr = new ArrayList<>();
                        curr.add(l);
                        bmap.put(b, curr);
                    } else {
                        bmap.get(b).add(l);
                    }
                }
                ArrayList<Integer> resultarray = new ArrayList<>();
                Iterator bmapIterator = bmap.entrySet().iterator();
                while (bmapIterator.hasNext()) {
                    Map.Entry bmapElement = (Map.Entry)bmapIterator.next();
                    ArrayList<Line> gongxian = (ArrayList<Line>)bmapElement.getValue();
                    HashSet<Point> currp = new HashSet<>();
                    for (int i = 0; i < gongxian.size(); i++) {
                        if (!currp.contains(gongxian.get(i).p1)) {
                            currp.add(gongxian.get(i).p1);
                        }
                        if (!currp.contains(gongxian.get(i).p2)) {
                            currp.add(gongxian.get(i).p2);
                        }
                    }
                    resultarray.add(currp.size());
                }
                int sum = 0;
                for (int i = 0; i < resultarray.size(); i++) {
                    sum+=resultarray.get(i);
                }
                if (sum%2 == 0) {
                    if (n-sum >=2) {
                        result = sum+2;
                    }else {
                        result = n;
                    }
                }else {
                    if (n -sum >=1) {
                        result = sum+1;
                    }else {
                        result = n;
                    }
                }
                results.add(result);
            }
            int max = 1;
            for (int i = 0; i < results.size(); i++) {
                if (max < results.get(i)) {
                    max = results.get(i);
                }
            }
            System.out.println("Case #" + (turn + 1) + ": " + max);
        }
    }
}
class Point {
    long x;
    long y;
    Point(long x, long y) {
        this.x = x;
        this.y = y;
    }
}
class Line {
    Point p1;
    Point p2;
    double b;
    double k;
    Line(Point x, Point y) {
        p1 = x;
        p2 = y;
        k = ((double)(p1.y-p2.y))/(double)(p1.x-p2.x);
        b = (double)p1.y - p1.x*(k);
    }
}