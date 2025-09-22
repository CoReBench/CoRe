import java.util.*;
import java.io.*;
public class Solution {
  public static void main(String[] args) {
    Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
    int t = in.nextInt();
    for (int i = 1; i <= t; ++i) {
      int n = in.nextInt();
      play(i, n, in);
    }
  }
  public static void play (int i, int n, Scanner in) {
    String result = "";
    boolean R = true;
    boolean P = true;
    boolean S = true;
    int j = 1;
    if (n == 1) {
        String input = in.nextLine();
        result += input;
        result += input;
        result += input;
        if (input.charAt(0) == 'P') {
            result += "S";
        }
        if (input.charAt(0) == 'R') {
            result += "P";    
        }
        if (input.charAt(0) == 'S') {
            result += "R";
        }   
    } else {
       while (j <= n) {
           if (R == true || P == true || S == true){
            String input = in.nextLine();
            if (input.charAt(0) == 'P') {
                R = false;
                P = false;
            }
            if (input.charAt(0) == 'R') {
                R = false;
                S = false;
            }
            if (input.charAt(0) == 'S') {
                S = false;
                R = false;
            }   
           }
            j++;
        }
        if (R == true) {
            result += "P";
        } else if (P == true) {
            result += "S";
        } else if (S == true) {
            result += "R";
        } else {
            result = "IMPOSSIBLE";
        }
    }
    System.out.println("Case #" + i + ": " + result);
  }
}