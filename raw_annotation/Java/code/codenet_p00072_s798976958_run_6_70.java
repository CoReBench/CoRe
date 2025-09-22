import java.util.Scanner;
public class Main{
	public static void main(String[] args){
        new Main().run();
    }
	public void run(){
		Scanner scan = new Scanner(System.in);
		while(scan.hasNext()){
			int n = scan.nextInt();
			if(n == 0){
				break;
			}
			int m = scan.nextInt();
			int[][] cost = new int[n][n];
			for(int i = 0;i < n;i++){
				for(int j = 0;j < n;j++){
					cost[i][j] = Integer.MAX_VALUE;
				}
			}
			for(int i = 0;i < m;i++){
				String[] str = scan.next().split(",");
				int a = Integer.parseInt(str[0]);
				int b = Integer.parseInt(str[1]);
				int c = Integer.parseInt(str[2]);
				cost[a][b] = c;
				cost[b][a] = c;
			}
			int count = 0;
			int min = 0;
			int ti = 0;
			int tj = 0;
			boolean[] fl = new boolean[n];
			for(int i = 0;i < n-1;i++){
				min = 0;
				for(int j = i+1;j < n;j++){
					if(cost[i][j] == Integer.MAX_VALUE){
						continue;
					}
					if(min == 0 || min > cost[i][j]){
						min = cost[i][j];
						ti = i;
						tj = j;
					}
				}
				if(min != 0){
					count += min/100 - 1;
					fl[ti] = true;
					fl[tj] = true;
				}
			}
			for(int i = 0;i < n;i++){
				if(fl[i]){
					continue;
				}
				min = 0;
				for(int j = 0;j < i;j++){
					if(cost[j][i] == Integer.MAX_VALUE){
						continue;
					}
					if(min == 0 || min > cost[j][i]){
						min = cost[j][i];
					}
				}
				if(min != 0){
					count += min/100 - 1;
				}
			}
			System.out.println(count);
		}
	}
}