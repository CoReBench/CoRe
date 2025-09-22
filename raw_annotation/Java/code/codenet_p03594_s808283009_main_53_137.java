import java.util.*;
import java.io.*;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.MathContext;
class Main
{
	static class Pair implements Comparable
	{
		int first;
		double second;
		public Pair(int f, double s)
		{
			first = f;
			second = s;
		}
		public String toString()
		{
			return first + " " + second;
		}
		public int compareTo(Object o)
		{
			Pair p2 = (Pair)o;
			if(this.first < p2.first)
				return -1;
			if(this.first > p2.first)
				return 1;
			if(this.second < p2.second)
				return -1;
			if(this.second > p2.second)
				return 1;
			return 0;
		}
	}
	static int log2(double a)
	{
		return (int)(Math.log(a) / Math.log(2));
	}
	static long gcd(long a, long b)
	{
		long r;
		while((r = a % b) > 0)
		{
			a = b;
			b = r;
		}
		return b;
	}
	static int distance(int i1, int j1, int i2, int j2)
	{
		return Math.abs(i1 - i2) + Math.abs(j1 - j2);
	}
	public static void main(String[] args) throws IOException
	{
		int h = in.nextInt();
		int w = in.nextInt();
		int d = in.nextInt();
		int[][] ans = new int[h][w];
		for(int i = 0; i < h; i ++)
			Arrays.fill(ans[i], -1);
		for(int i = 0; i < h; i ++)
		{
			for(int j = 0; j < w; j ++)
			{
				boolean[] not = new boolean[4];
				int x = j + d;
				int y = i;
				for(; y <= i + d; x --, y ++)
				{
					if(x >= w)
						continue;
					if(y >= h)
						continue;
					if(ans[y][x] != -1)
					{
						not[ans[y][x]] = true;
					}
				}
				x = j + d;
				y = i;
				for(; y >= i - d; x --, y --)
				{
					if(x >= w)
						continue;
					if(y < 0)
						continue;
					if(ans[y][x] != -1)
					{
						not[ans[y][x]] = true;
					}
				}
				x = j - d;
				y = i;
				for(; y <= i + d; x ++, y ++)
				{
					if(x < 0)
						continue;
					if(y >= h)
						continue;
					if(ans[y][x] != -1)
					{
						not[ans[y][x]] = true;
					}
				}
				x = j - d;
				y = i;
				for(; y >= i - d; x ++, y --)
				{
					if(x < 0)
						continue;
					if(y < 0)
						continue;
					if(ans[y][x] != -1)
					{
						not[ans[y][x]] = true;
					}
				}
				for(int z = 0; z < 4; z ++)
				{
					if(!not[z])
					{
						ans[i][j] = z;
						break;
					}
				}
			}
		}
		char[] c = {'R', 'Y', 'G', 'B'};
		for(int i = 0; i < h; i ++)
		{
			for(int j = 0; j < w; j ++)
			{
				sop(c[ans[i][j] != -1 ? ans[i][j] : 0]);
			}
			sop("\n");
		}
	}
	static class FastReader
    {
        BufferedReader br;
        StringTokenizer st;
        public FastReader()
        {
            br = new BufferedReader(new InputStreamReader(System.in));
        }
        String next()
        {
            while (st == null || !st.hasMoreElements())
            {
                try
                {
                    st = new StringTokenizer(br.readLine());
                }
                catch (IOException  e)
                {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        int nextInt()
        {
            return Integer.parseInt(next());
        }
        long nextLong()
        {
            return Long.parseLong(next());
        }
        double nextDouble()
        {
            return Double.parseDouble(next());
        }
        String nextLine()
        {
            String str = "";
            try
            {
                str = br.readLine();
            }
            catch (IOException e)
            {
                e.printStackTrace();
            }
            return str;
        }
    }
    static FastReader in = new FastReader();
    public static void sop(Object o)
    {
    	System.out.print(o);
    }
}