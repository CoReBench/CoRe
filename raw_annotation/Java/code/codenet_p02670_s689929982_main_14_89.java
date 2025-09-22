import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.PriorityQueue;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.HashSet;
public class Main {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int n = fs.nextInt();
        boolean flag = true;
        int[][] m = new int[n][n];
        int x = 1;
        int count = 0;
        List<ArrayList<Integer>> graph = new ArrayList<>();
        boolean[] exist = new boolean[n*n];
        boolean[] possible = new boolean[n*n];
        Arrays.fill(exist,true);
        Arrays.fill(possible,false);
        HashSet<Integer> set = new HashSet<Integer>();
        Queue<Integer> queue = new ArrayDeque<>();
        for(int i = 0; i < n; i++){
          for(int j = 0; j < n; j++){
            List<Integer> near = new ArrayList<>();
            graph.add(new ArrayList<>());
            if(i == 0 || i == n-1 || j == 0 || j == n-1){
              set.add(x);
            }
            if(x - 1 > i*n){
              graph.get(x-1).add(x-1);
            }
            if(x + 1 <= n*(i+1)){
              graph.get(x-1).add(x+1);
            }
            if(x - n > 0){
              graph.get(x-1).add(x-n);
            }
            if(x + n <= n*n){
              graph.get(x-1).add(x+n);
            }
            int p = fs.nextInt();
            queue.add(p);
            m[i][j] = x;
            x += 1;
          }
        }
        while(queue.size() > 0){
          int a = queue.poll();
          exist[a-1] = false;
          if(set.contains(a)){
            possible[a-1] = true;
          }
          if(possible[a-1] == true){
            for(int w : graph.get(a-1)){
              possible[w-1] = true;
            }
          }
          else{
            for(int w : graph.get(a-1)){
              if(possible[w-1] == true && exist[w-1] == false){
                possible[a-2] = true;
                possible[a-1-n] = true;
                possible[a] = true;
                possible[a-1+n] = true;
                possible[a-1] = true;
                count -= 1;
                break;
              }
            }
            count += 1;
            if(a-2 >= 0 || a-1-n >= 0 || a <= n*n || a-1+n <= n*n){
              if((exist[a-2] == false && possible[a-2] == true) || (exist[a-1-n] == false && possible[a-1-n] == true) || (exist[a] == false && possible[a] == true) || (exist[a-1+n] == false && possible[a-1+n] == true)){
                possible[a-2] = true;
                possible[a-1-n] = true;
                possible[a] = true;
                possible[a-1+n] = true;
                possible[a-1] = true;
              }
            }
          }
        }
        System.out.print(count);
  }
}
class FastScanner {
    private final InputStream in = System.in;
    private final byte[] buffer = new byte[1024];
    private int ptr = 0;
    private int buflen = 0;
    private boolean hasNextByte(){
        if(ptr < buflen){
            return true;
        }else{
            ptr = 0;
            try{
                buflen = in.read(buffer);
            }catch(IOException e){
                e.printStackTrace();
            }
            if(buflen <=0){
                return false;
            }
        }
        return true;
    }
    private int readByte(){
        if(hasNextByte())return buffer[ptr++];
        else return -1;
    }
    private static boolean isPrintableChar(int c){
        return 33<=c && c<=126;
    }
    public boolean hasNext(){
        while(hasNextByte() && !isPrintableChar(buffer[ptr]))ptr++;
        return hasNextByte();
    }
    public String next(){
        if(!hasNext()) throw new NoSuchElementException();
        StringBuilder sb = new StringBuilder();
        int b = readByte();
        while(isPrintableChar(b)){
            sb.appendCodePoint(b);
            b = readByte();
        }
        return sb.toString();
    }
    public long nextLong(){
        if(!hasNext()) throw new NoSuchElementException();
        long n = 0;
        boolean minus = false;
        int b = readByte();
        if(b == '-'){
            minus = true;
            b = readByte();
        }
        if(b < '0' || '9' < b){
            throw new NumberFormatException();
        }
        while(true){
            if('0' <= b && b<='9'){
                n*=10;
                n+=b-'0';
            }else if(b==-1 || !isPrintableChar(b)){
                return minus ? -n : n;
            }else{
                throw new NumberFormatException();
            }
            b = readByte();
        }
    }
    public int nextInt(){
        long nl = nextLong();
        if(nl < Integer.MIN_VALUE || nl > Integer.MAX_VALUE)throw new NumberFormatException();
        return (int) nl;
    }
    public double nextDoutble(){return Double.parseDouble(next());}
}