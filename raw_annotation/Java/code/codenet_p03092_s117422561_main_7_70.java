import java.io.IOException;
import java.io.InputStream;
import java.util.NoSuchElementException;
public class Main {
    private static FastScanner sc = new FastScanner();
    private static boolean DEBUG_FLG = false;
    public static void main(String[] args) {
    	int N = sc.nextInt();
    	long A = sc.nextLong();
    	long B = sc.nextLong();
    	int[] p = new int[N];
    	for(int i=0; i<N; i++) {
    		p[i] = sc.nextInt();
    	}
    	long[][] dpc = new long[N][N];
    	int[][] dpmin = new int[N][N];
    	int[][] dpmin2 = new int[N][N];
    	int[][] dpmax = new int[N][N];
    	int[][] dpmax2 = new int[N][N];
    	for(int i=0; i<N; i++) {
    		dpc[i][i] = 0;
    		dpmin[i][i] = p[i];
    		dpmax[i][i] = p[i];
    		dpmin2[i][i] = Integer.MAX_VALUE;
    		dpmax2[i][i] = -1;
    	}
    	for(int d=1; d<N; d++) {
    		for(int i=0; i<N-d; i++) {
    			if(p[i+d] < dpmin[i][i+d-1]) {
    				dpmin2[i][i+d] = dpmin[i][i+d-1];
    				dpmin[i][i+d] = p[i+d];
    			} else if(p[i+d] < dpmin2[i][i+d-1]) {
    				dpmin2[i][i+d] = p[i+d];
    				dpmin[i][i+d] = dpmin[i][i+d-1];
    			} else {
    				dpmin2[i][i+d] = dpmin2[i][i+d-1];
    				dpmin[i][i+d] = dpmin[i][i+d-1];
    			}
    			if(p[i+d] > dpmax[i][i+d-1]) {
    				dpmax2[i][i+d] = dpmax[i][i+d-1];
    				dpmax[i][i+d] = p[i+d];
    			} else if(p[i+d] > dpmax2[i][i+d-1]) {
    				dpmax2[i][i+d] = p[i+d];
    				dpmax[i][i+d] = dpmax[i][i+d-1];
    			} else {
    				dpmax2[i][i+d] = dpmax2[i][i+d-1];
    				dpmax[i][i+d] = dpmax[i][i+d-1];
    			}
    			long rightcost = 0;
    			if(p[i+d] > dpmax[i][i+d-1]) {
    				rightcost = dpc[i][i+d-1];
    			} else if(p[i+d] >  dpmax2[i][i+d-1]){
    				rightcost = dpc[i][i+d-1] + Math.min(A, B);
    			} else {
    				rightcost = dpc[i][i+d-1] + B;
    			}
    			long leftcost = 0;
    			if(p[i] < dpmin[i+1][i+d]) {
    				leftcost = dpc[i+1][i+d];
    			} else if(p[i] < dpmin2[i+1][i+d]){
    				leftcost = dpc[i+1][i+d] + Math.min(A, B);
    			} else {
    				leftcost = dpc[i+1][i+d] + A;
    			}
    			dpc[i][i+d] = Math.min(leftcost, rightcost);
    			debug(i, i+d, leftcost, rightcost, dpmin[i][i+d], dpmin2[i][i+d], dpmax[i][i+d], dpmax2[i][i+d]);
    		}
    	}
    	System.out.println(dpc[0][N-1]);
    }
    static void debug(long... args) {
    	if(!DEBUG_FLG) return;
    	boolean flg = false;
    	for(long s : args) {
    		if(flg) System.out.print(" ");
    		flg = true;
    		System.out.print(s);
    	}
    	System.out.println();
    }
    static class FastScanner {
        private final InputStream in = System.in;
        private final byte[] buffer = new byte[1024];
        private int ptr = 0;
        private int buflen = 0;
        private boolean hasNextByte() {
            if(ptr < buflen) {
                return true;
            } else {
                ptr = 0;
                try {
                    buflen = in.read(buffer);
                } catch(IOException e) {
                    e.printStackTrace();
                }
                if(buflen <= 0) {
                    return false;
                }
            }
            return true;
        }
        private int readByte() { if (hasNextByte()) return buffer[ptr++]; else return -1;}
        private static boolean isPrintableChar(int c) { return 33 <= c && c <= 126;}
        private void skipUnprintable() { while(hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++;}
        public boolean hasNext() { skipUnprintable(); return hasNextByte();}
        public String next() {
            if (!hasNext()) throw new NoSuchElementException();
            StringBuilder sb = new StringBuilder();
            int b = readByte();
            while(isPrintableChar(b)) {
                sb.appendCodePoint(b);
                b = readByte();
            }
            return sb.toString();
        }
        public long nextLong() {
            return Long.parseLong(next());
        }
        public int nextInt(){
            return Integer.parseInt(next());
        }
        public double nextDouble(){
            return Double.parseDouble(next());
        }
    }
}