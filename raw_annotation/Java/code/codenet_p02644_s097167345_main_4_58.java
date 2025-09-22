import java.io.*;
import java.util.*;
public class Main{
	static void main() throws Exception{
		int n=sc.nextInt(),m=sc.nextInt(),k=sc.nextInt();
		int[]start=new int[2],end=new int[2];
		for(int i=0;i<2;i++) {
			start[i]=sc.nextInt()-1;
		}
		for(int i=0;i<2;i++) {
			end[i]=sc.nextInt()-1;
		}
		char[][]in=new char[n][m];
		for(int i=0;i<n;i++)
			in[i]=sc.nextLine().toCharArray();
		int inf=(int)1e9;
		int[][][]dist=new int[n][m][4];
		for(int[][]i:dist)
			for(int[]j:i)
				Arrays.fill(j, inf);
		LinkedList<int[]>q=new LinkedList<>();
		q.add(new int[] {start[0],start[1],k,-1,0});
		dist[start[0]][start[1]][0]=0;
		dist[start[0]][start[1]][1]=0;
		dist[start[0]][start[1]][2]=0;
		dist[start[0]][start[1]][3]=0;
		int[]dx= {0,1,0,-1},dy= {1,0,-1,0};
		while(!q.isEmpty()) {
			int cur[]=q.poll();
			int x=cur[0],y=cur[1],curK=cur[2],dir=cur[3];
			int curDist=cur[4];
			for(int i=0;i<4;i++) {
				int xx=x+dx[i],yy=y+dy[i];
				if(xx<0 || xx>=n || yy<0 || yy>=m || dist[xx][yy][(i)]!=inf || in[xx][yy]=='@')continue;
				int[]nxt=new int[] {xx,yy,curK-1,(i),0};
				if(nxt[2]<0) {
					nxt[2]=k-1;
					dist[xx][yy][(i)]=curDist+1;
				}
				else {
					if(dir==(i)) {
						dist[xx][yy][(i)]=curDist;
					}
					else {
						dist[xx][yy][(i)]=curDist+1;
						nxt[2]=k-1;
					}
				}
				nxt[4]=dist[xx][yy][(i)];
				q.add(nxt);
			}
		}
		int ans=inf;
		for(int i=0;i<4;i++) {
			ans=Math.min(ans, dist[end[0]][end[1]][i]);
		}
		pw.println(ans==inf?-1:ans);
	}
	public static void main(String[] args) throws Exception{
		pw=new PrintWriter(System.out);
		sc = new MScanner(System.in);
			main();
		pw.flush();
	}
	static PrintWriter pw;
	static MScanner  sc;
	static class MScanner {
		StringTokenizer st;
		BufferedReader br;
		public MScanner(InputStream system) {
			br = new BufferedReader(new InputStreamReader(system));
		}
		public MScanner(String file) throws Exception {
			br = new BufferedReader(new FileReader(file));
		}
		public String next() throws IOException {
			while (st == null || !st.hasMoreTokens())
				st = new StringTokenizer(br.readLine());
			return st.nextToken();
		}
		public int[] intArr(int n) throws IOException {
	        int[]in=new int[n];for(int i=0;i<n;i++)in[i]=nextInt();
	        return in;
		}
		public long[] longArr(int n) throws IOException {
	        long[]in=new long[n];for(int i=0;i<n;i++)in[i]=nextLong();
	        return in;
		}
		public int[] intSortedArr(int n) throws IOException {
	        int[]in=new int[n];for(int i=0;i<n;i++)in[i]=nextInt();
	        shuffle(in);
	        Arrays.sort(in);
	        return in;
		}
		public long[] longSortedArr(int n) throws IOException {
	        long[]in=new long[n];for(int i=0;i<n;i++)in[i]=nextLong();
	        shuffle(in);
	        Arrays.sort(in);
	        return in;
		}
		public Integer[] IntegerArr(int n) throws IOException {
	        Integer[]in=new Integer[n];for(int i=0;i<n;i++)in[i]=nextInt();
	        return in;
		}
		public Long[] LongArr(int n) throws IOException {
	        Long[]in=new Long[n];for(int i=0;i<n;i++)in[i]=nextLong();
	        return in;
		}
		public String nextLine() throws IOException {
			return br.readLine();
		}
		public int nextInt() throws IOException {
			return Integer.parseInt(next());
		}
		public double nextDouble() throws IOException {
			return Double.parseDouble(next());
		}
		public char nextChar() throws IOException {
			return next().charAt(0);
		}
		public long nextLong() throws IOException {
			return Long.parseLong(next());
		}
		public boolean ready() throws IOException {
			return br.ready();
		}
		public void waitForInput() throws InterruptedException {
			Thread.sleep(3000);
		}
	}
	static void shuffle(int[]in) {
		for(int i=0;i<in.length;i++) {
			int idx=(int)(Math.random()*in.length);
			int tmp=in[i];
			in[i]=in[idx];
			in[idx]=tmp;
		}
	}
	static void shuffle(long[]in) {
		for(int i=0;i<in.length;i++) {
			int idx=(int)(Math.random()*in.length);
			long tmp=in[i];
			in[i]=in[idx];
			in[idx]=tmp;
		}
	}
}