import java.util.Scanner;
public class Main {
	StringBuffer max;
	public static void main(String[] args) {
		new Main().run();
	}
	private void run() {
		Scanner scan = new Scanner(System.in);
		String[] b = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"};
		String[] s = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"};
		max = new StringBuffer();
		while (scan.hasNext()) {
			String min = scan.next();
			for (int i = 0; i < min.length(); i++) {
				String str = min.substring(i, i+1);
				if (str.equals(".")) {
					max.append(str);
				}else {
					for (int j = 0; j < s.length; j++) {
						if (str.equals(s[j])) {
							max.append(b[j]);
							continue;
						}
					}
				}
			}
			max.append(" ");
		}
		max.delete(max.length()-1, max.length());
		System.out.println(max);
	}
	private void debug() {
		System.out.println();
	}
}