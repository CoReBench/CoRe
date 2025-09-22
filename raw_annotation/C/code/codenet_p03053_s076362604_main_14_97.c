#include <stdio.h>
int max(int a, int b){
	if(a>b){
		return a;
	}
	return b;
}
int min(int a, int b){
	if(a>b){
		return b;
	}
	return a;
}
int main(){
	int H;
	scanf("%d",&H);
	int W;
	scanf("%d",&W);
	char c;
	char d;
	char l[1001][1001];
	int i;
	int j;
	for(i=1;i<=H;i++){
		scanf("%c",&d);
		for(j=1;j<=W;j++){
			scanf("%c",&c);
			l[i][j]=c;
		}
	}
	int m;
	m=H+W;
	int p[1001][1001];
	int q[1002][1001];
	int r[1001][1002];
	int s[1002][1002];
	for(i=1;i<=H;i++){
		p[i][0]=m;
		q[i][W+1]=m;
		r[i][0]=m;
		s[i][W+1]=m;
	}
	for(j=1;j<=W;j++){
		p[0][j]=m;
		q[0][j]=m;
		r[H+1][j]=m;
		s[H+1][j]=m;
	}
	for(i=1;i<=H;i++){
		for(j=1;j<=W;j++){
			if(l[i][j]=='#'){
				p[i][j]=0;
			}else{
				p[i][j]=min(p[i-1][j],p[i][j-1])+1;
			}
		}
	}
	for(i=1;i<=H;i++){
		for(j=W;j>=1;j--){
			if(l[i][j]=='#'){
				q[i][j]=0;
			}else{
				q[i][j]=min(q[i-1][j],q[i][j+1])+1;
			}
		}
	}
	for(i=H;i>=1;i--){
		for(j=1;j<=W;j++){
			if(l[i][j]=='#'){
				r[i][j]=0;
			}else{
				r[i][j]=min(r[i+1][j],r[i][j-1])+1;
			}
		}
	}
	for(i=H;i>=1;i--){
		for(j=W;j>=1;j--){
			if(l[i][j]=='#'){
				s[i][j]=0;
			}else{
				s[i][j]=min(s[i+1][j],s[i][j+1])+1;
			}
		}
	}
	int n[1001][1001];
	int ans;
	ans=0;
	for(i=1;i<=H;i++){
		for(j=1;j<=W;j++){
			n[i][j]=min(p[i][j],q[i][j]);
			n[i][j]=min(n[i][j],r[i][j]);
			n[i][j]=min(n[i][j],s[i][j]);
			ans=max(ans,n[i][j]);
		}
	}
	printf("%d",ans);
}