import java.util.*;
public class Main {
    public static class time implements Comparable<time>{
        long a;
        long b;
        void time(long x,long y){
            this.a=x;
            this.b=y;
        }
        public int compareTo(time t){
            if(this.a==t.a){
                return (int)(this.b-t.b);
            }else{
                return (int)(this.a-t.a);
            }
        }
        public void tostring(){
            System.out.print("[ "+this.a+" , "+this.b+" ]");
        }
    }
    public static long TIME(long a,long b,long t){
        return (t-b)/(a+1);
    }
    public static void main(String[] args) throws Exception {
        Scanner sc=new Scanner(System.in);
        int N=sc.nextInt();
        long T=sc.nextLong();
        time[] ROOT=new time[N];
        for(int i=0;i<N;i++){
            time tm=new time();
            tm.a=sc.nextLong();
            tm.b=sc.nextLong();
            ROOT[i]=tm;
        }
        Arrays.sort(ROOT);
        int idx=0;
        int ans=0;
        while(T>0&&idx<N){
            T=(T-ROOT[idx].b)/(ROOT[idx].a+1);
            ans++;
            idx++;
            if(idx==N-1){
                ans++;
            }
        }
        ans--;
        System.out.println(ans);
    }
}