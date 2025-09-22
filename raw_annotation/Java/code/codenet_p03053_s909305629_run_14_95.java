import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.StringReader;
import java.util.ArrayList;
import java.util.StringTokenizer;
import java.util.Scanner;
public class Main  implements Runnable { 
    public static void main(String[] args) {
        new Thread(null, new Main(), "", 16 * 1024 * 1024).start(); 
    }
    public void run() {
    	Scanner sc = new Scanner(System.in);
		int h = Integer.parseInt(sc.next());
		int w = Integer.parseInt(sc.next());
		char a[][] = new char[h][w];
		int atmp[] = new int[h];
		int max= 0;
		int blackar[][] = new int[h*w][2];
		int p=0;
		for (int i = 0; i < h; i++)
		{
				a[i]= sc.next().toCharArray();
				for (char j = 0; j < w; j++)
				{
					if(a[i][j]=='#')
					{
						blackar[p][0]=i;
						blackar[p][1]=j;
						p++;
					}
				}
		}
		int maxp = p;
    	int p2=p;
		p=0;
	    while(p<h*w)
	    {
		    int hap = 0;
			for (; p<maxp;p++)
			{
				int i = blackar[p][0];
				int j = blackar[p][1];
					if(i-1>=0)
					{
						if (a[i-1][j] == '.')
						{
							a[i-1][j] = '#';
							blackar[p2][0]=i-1;
							blackar[p2][1]=j;
							p2++;
						}
					}
					if(j-1>=0)
					{
						if (a[i][j-1] == '.')
						{
							a[i][j-1] = '#';
							blackar[p2][0]=i;
							blackar[p2][1]=j-1;
							p2++;
						}
					}
					if(i+1<h)
					{
						if (a[i+1][j] == '.')
						{
							a[i+1][j] = '#';
							blackar[p2][0]=i+1;
							blackar[p2][1]=j;
							p2++;
						}
					}
					if(j+1<w)
					{
						if (a[i][j+1] == '.')
						{
							a[i][j+1] = '#';
							blackar[p2][0]=i;
							blackar[p2][1]=j+1;
							p2++;
						}
					}
		    }
			maxp=p2;
			max++;
		}
	    max= max-1;
		int ans = max;
		PrintWriter out = new PrintWriter(System.out);
		out.println(ans);
		out.flush();
	}
    static class FastScanner {
        private BufferedReader reader = null;
        private StringTokenizer tokenizer = null;
        public FastScanner(String in) {
        	StringReader sr = new StringReader(in);
            reader = new BufferedReader(new BufferedReader(sr));
            tokenizer = null;
        }
        public FastScanner(InputStream in) {
            reader = new BufferedReader(new InputStreamReader(in));
            tokenizer = null;
        }
        public String next() {
            if (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }
        public String nextLine() {
            if (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    return reader.readLine();
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken("\n");
        }
        public long nextLong() {
            return Long.parseLong(next());
        }
        public long nextInt() {
            return Integer.parseInt(next());
        }
    }
}