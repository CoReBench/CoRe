#include<stdio.h>
#include<stdlib.h>
#define min(a,b) ((a)>(b)?(b):(a))
int popcount(int n){
	if(!n)return 0;
	return (n&1) + popcount(n>>1);
}
int main(){
	int N, X[20], Y[20], P[20], a[20];
	long Z[1<<16][16][2], ans[20]={1l<<60};
	scanf("%d", &N);
	for(int i=0; i<N; i++){
		scanf("%d%d%d", X+i, Y+i, P+i);
		ans[i+1] = 1l<<60;
	}
	for(int i=0; i<(1<<N); i++){
		for(int j=0; j<N; j++){
			Z[i][j][0] = abs(X[j]);
			Z[i][j][1] = abs(Y[j]);
			for(int k=0; k<N; k++){
				if((i>>k)&1){
					Z[i][j][0] = min(Z[i][j][0], (long)abs(X[j]-X[k]));
					Z[i][j][1] = min(Z[i][j][1], (long)abs(Y[j]-Y[k]));
				}
			}
		}
	}
	while(!a[N]){
		int h=0, v=0;
		for(int i=0; i<N; i++){
			if(a[i]==1)	
				h |= (1<<i);
			if(a[i]==2)	
				v |= (1<<i);
		}
		int t = popcount(h|v);
		long sum = 0;
		for(int i=0; i<N; i++){
			sum += (long)P[i] * min(Z[h][i][0], Z[v][i][1]);
		}
		int i=0;
		while(a[i]==2)
			a[i++]=0;
		a[i]++;
		ans[t] = min(ans[t], sum);
	}
	for(int i=0; i<=N; i++){
		printf("%ld\n", ans[i]);
	}
	return 0;
}