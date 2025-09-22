import java.io.*;
import java.lang.*;
import java.util.*;
public class Solution{
    static class Pair implements Comparable<Pair>{
        long value;
        int count;
        public Pair(long value,int count){
            this.value = value;
            this.count = count;
        }
        @Override
        public int compareTo(Pair o){
            return o.count - this.count;
        }
    }
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = new Integer(br.readLine());
        StringBuffer sb = new StringBuffer();
        for(int z=1;z<=t;z++){
            sb.append("Case #"+z+": ");
            StringTokenizer st = new StringTokenizer(br.readLine());
            StringTokenizer st1 = new StringTokenizer(br.readLine());
            int n = new Integer(st.nextToken());
            int d = new Integer(st.nextToken());
            if(n==1&&d==3){
                sb.append("2\n");
                continue;
            }
            else if(n==1&&d==2){
                sb.append("1\n");
                continue;
            }
            long[] array = new long[n];
            for(int i=0;i<n;i++){
                array[i]=new Long(st1.nextToken());
            }
            Arrays.sort(array);
            Pair[] ps = new Pair[n];
            int w=0;
            int count = 1;
            for(int i=1;i<n;i++){
                if(array[i]==array[i-1]){
                    count++;
                }
                else{
                    ps[w++]=new Pair(array[i-1],count);
                    count=1;
                }
            }
            ps[w++]=new Pair(array[n-1],count);
            Arrays.sort(ps,0,w);
            if(ps[0].count>=d){
                sb.append("0\n");
                continue;
            }
            else{
                if(d==2&&ps[0].count==1){
                    sb.append("1\n");
                    continue;
                }
                else if(d==3&&ps[0].count==2&&ps[0].value!=array[n-1]){
                    sb.append("1\n");
                    continue;
                }
                else if(d==3&&ps[0].count==2&&ps[0].value==array[n-1]){
                    if(ps[1].count==2){
                        sb.append("1\n");
                        continue;
                    }
                    boolean flag = false;
                    outer:for(int i=0;i<n;i++){
                        for(int j=0;j<n;j++){
                            if(array[j]==2*array[i]||array[i]==2*array[j]){
                                sb.append("1\n");
                                flag = true;
                                break outer;
                            }
                        }
                    }
                    if(!flag){
                        sb.append("2\n");
                        continue;
                    }
                }
                else if(d==3&&ps[0].count==1){
                    boolean flag = false;
                    outer:for(int i=0;i<n;i++){
                        for(int j=0;j<n;j++){
                            if(array[j]==2*array[i]||array[i]==2*array[j]){
                                sb.append("1\n");
                                flag = true;
                                break outer;
                            }
                        }
                    }
                    if(!flag){
                        sb.append("2\n");
                        continue;
                    }
                }
            }
        }
        br.close();
        System.out.println(sb);
    }
}