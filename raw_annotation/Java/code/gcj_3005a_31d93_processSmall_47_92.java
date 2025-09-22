import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.util.ArrayList;
import java.util.List;
public class Solution {
    public static void main(String[] args) {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        try {
            int t = Integer.parseInt(bufferedReader.readLine());
            List<List<String>> caseList = new ArrayList(t);
            for (int testCaseNum = 0; testCaseNum < t; testCaseNum++) {
                List<String> singleCase = new ArrayList<>();
                String rchv = bufferedReader.readLine();
                singleCase.add(rchv);
                int n = Integer.parseInt(rchv.split(" ")[0]);
                for (int i =0; i<n; i++) {
                    singleCase.add(bufferedReader.readLine());
                }
                caseList.add(singleCase);
            }
            int b = 0;
            for (List<String> singleCase : caseList) {
                b++;
                if (processCase(singleCase)) {
                    System.out.println("Case #"+b+": POSSIBLE");
                } else {
                    System.out.println("Case #"+b+": IMPOSSIBLE");
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    public static boolean processCase(List<String> caseList) {
        int[] rchv = new int[4];
        String[] split = caseList.get(0).split(" ");
        for (int i = 0; i < rchv.length; i++){
            rchv[i] = Integer.parseInt(split[i]);
        }
        if (rchv[1] < 10 && rchv[0] < 10 && rchv[2] == 1 && rchv[3] == 1) {
            return processSmall(rchv, caseList);
        }
        return false;
    }
    public static boolean processSmall(int[] rchv, List<String> caseList) {
        List<int[]> chipCoords = new ArrayList<>();
        List<Integer> xCoords = new ArrayList<>();
        List<Integer> yCoords = new ArrayList<>();
        for (int i = 0; i < rchv[0]; i++) {
            String row = caseList.get(i+1);
            String[] split = row.split("");
            for (int j = 0; j < rchv[1]; j++) {
                if ("@".equals(split[j])) {
                    int[] coords = new int[2];
                    coords[0] = i;
                    xCoords.add(i);
                    coords[1] = j;
                    yCoords.add(j);
                    chipCoords.add(coords);
                }
            }
        }
        for (int x =0; x<rchv[0]; x++) {
            for (int y = 0; y< rchv[1]; y++) {
                int topright = 0;
                int topleft = 0;
                int bottomLeft = 0;
                int bottomRight = 0;
                for (int z = 0; z < chipCoords.size(); z++) {
                    if (chipCoords.get(z)[0] <= x) {
                        if (chipCoords.get(z)[1] <= y) {
                            bottomLeft ++;
                        } else {
                            bottomRight ++;
                        }
                    } else {
                        if (chipCoords.get(z)[1] < y) {
                            topleft ++;
                        } else {
                            topright ++;
                        }
                    }
                }
                if (bottomRight == bottomLeft && bottomLeft == topleft && topleft == topright) {
                    return true;
                }
            }
        }
        return false;
    }
}