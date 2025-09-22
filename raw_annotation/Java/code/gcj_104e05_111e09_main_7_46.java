import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.TreeSet;
public class Solution {
	public static void main(String[] args)throws IOException
    {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int tc = Integer.parseInt(br.readLine()); 
		for(int i=0; i<tc; i++) {
			int noOfWords = Integer.parseInt(br.readLine()); 
			TreeSet<String> set = new TreeSet<String>();
			for(int j=0; j<noOfWords; j++) {
				String word = br.readLine();
				set.add(word);
			}
			Iterator<String> wrd1 = set.iterator();
			Iterator<String> wrd2 = set.iterator();
			int c1 = 0;
			while(wrd1.hasNext()) {
				c1++;
				int c2 = 0;
				String wordOne = wrd1.next();
				int result = 0;
				while(wrd2.hasNext()) {
					c2++;
					if(c1 != c2) {
						String wordTwo = wrd2.next();
						int max = 0;
						String key = "";
						for(int l = 0; l< wordTwo.length()-1; l++) {
							for(int k = l+2; k<=wordTwo.length(); k++) {
								if(wordOne.contains(wordTwo.substring(l, k)) && k-l > max) {
									max = k-l;
									key = wordTwo.substring(l, k);
								}else {
									break;
								}
							}
						}
					}
				}
			}
		}
	}
}
 class Longest_common_substr { 
    static int printLCSubStr(String X, String Y, int m, int n) {
        int[][] LCSuff = new int[m + 1][n + 1]; 
        int len = 0; 
        int row = 0, col = 0; 
        for (int i = 0; i <= m; i++) { 
            for (int j = 0; j <= n; j++) { 
                if (i == 0 || j == 0) 
                    LCSuff[i][j] = 0; 
                else if (X.charAt(i - 1) == Y.charAt(j - 1)) { 
                    LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1; 
                    if (len < LCSuff[i][j]) { 
                        len = LCSuff[i][j]; 
                        row = i; 
                        col = j; 
                    } 
                } 
                else
                    LCSuff[i][j] = 0; 
            } 
        } 
        if (len == 0) { 
            return 0; 
        } 
        String resultStr = ""; 
        while (LCSuff[row][col] != 0) { 
            resultStr = X.charAt(row - 1) + resultStr; 
            --len; 
            row--; 
            col--; 
        } 
        return resultStr.length(); 
    } 
    public static void main(String args[]) throws IOException 
    { 
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int tc = Integer.parseInt(br.readLine()); 
		for(int i=1; i<=tc; i++) {
			int noOfWords = Integer.parseInt(br.readLine()); 
			TreeSet<String> set = new TreeSet<String>();
			for(int j=0; j<noOfWords; j++) {
				String word = br.readLine();
				set.add(word);
			}
			Iterator<String> wrd1 = set.iterator();
			Iterator<String> wrd2 = set.iterator();
			int c1 = 0, result = 0;
			while(wrd1.hasNext()) {
				int max = 0;
				String key1 = "";
				String key2 = "";
				String w1 = wrd1.next();
				if(w1.equals(key1)) {
					wrd1.remove();
					return;
				}
				while(wrd2.hasNext()) {
					String w2 = wrd2.next();
					if(w2.equals(key2)) {
						wrd2.remove();
						return;
					}
				int count =printLCSubStr(w1,w2,w1.length(),w2.length());
				if(count > max) {
					key1 = w1;
					key2 = w2;
					max = count;
				}
				}
				result = result + max;
			}
			System.out.println("Case #"+i+": "+result);
		}
    } 
}