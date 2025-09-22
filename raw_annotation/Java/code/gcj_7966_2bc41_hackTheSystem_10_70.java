import java.util.Scanner;
public class Solution {
    static Long shootDamage;
    static Long shootCounter;
    static Long shield;
    static String code;
    static Long damage;
    static Long movements;
    static int lastIterableElement;
    public static String hackTheSystem(String[] softwareToHack) {
        shootDamage = 1L;
        shootCounter = 0L;
        shield = Long.parseLong(softwareToHack[0]);
        code = softwareToHack[1];
        damage = 0L;
        movements = 0L;
        int sizeScript = code.length() - 1;
        lastIterableElement = sizeScript;
        for (int i = 0; i < code.length(); i++) {
            if (code.charAt(i) == 'S') {
                damage += shootDamage;
                shootCounter++;
            }
            if (code.charAt(i) == 'C') {
                shootDamage *= 2;
            }
        }
        if (damage <= shield) {
            return String.valueOf(movements);
        }
        if (shootCounter > shield) {
            return "IMPOSSIBLE";
        }
        for (int i = sizeScript; i >= 0; i--) {
            for (int j = sizeScript - 1; j >= 0; j--) {
                if(code.charAt(j) == 'S' && code.charAt(i) == 'S') {
                    i--;
                    continue;
                }
                if(code.charAt(i) == 'C') {
                    shootDamage /= 2;
                    i--;
                    lastIterableElement--;
                    continue;
                }
                if (code.charAt(j) == 'C' && code.charAt(i) == 'S') {
                    movements++;
                    damage -= (shootDamage / 2);
                    char[] c = code.toCharArray();
                    if (damage <= shield) {
                        return String.valueOf(movements);
                    }
                    char temp = c[j];
                    c[j] = c[i];
                    c[i] = temp;
                    code = String.valueOf(c);
                    if (i == lastIterableElement) {
                        shootDamage /= 2;
                        if(i>0) {
                            i--;
                        }
                    } else {
                        i++;
                        j += 2;
                    }
                }
            }
        }
        return String.valueOf(movements);
    }
    private static final Scanner scan = new Scanner(System.in);
    public static void main(String[] args) {
        int numberOfCases = Integer.parseInt(scan.nextLine());
        String[][] cases = new String[numberOfCases][2];
        for (int i = 0; i < numberOfCases; i++) {
            String[] caseNumber = scan.nextLine().split(" ");
            cases[i][0] = caseNumber[0];
            cases[i][1] = caseNumber[1];
        }
        for (int i = 0; i < numberOfCases; i++) {
            System.out.println("Case #" + i + ": " + hackTheSystem(cases[i]));
        }
    }
}