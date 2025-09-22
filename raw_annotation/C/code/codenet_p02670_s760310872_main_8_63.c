#include<stdio.h>
#include<math.h>
#include<stdlib.h>
long compare_int(const void *a,const void *b)
{
	return *(long*)a-*(long*)b;
}
int main(void)
{
	int n;
	scanf("%d",&n);
	int a[501][501];
	long p,k=1,cnt=0;
	for(int i=0;i<n;i++) {
		for(int j=0;j<n;j++) {
			a[i][j]=k;
			k++;
		}
	}
	for(int ii=0;ii<(n*n);ii++) {
		scanf("%ld",&p);
		if(1<=p&&n>=p) {
			a[0][p-1]=0;
		}
		else if((n*n)>=p&&((n*n)-n+1)<=p) {
			a[n-1][n-(n*n)+p-1]=0;
		} else if (p%n==0) {	
				a[(p/n)-1][n-1]=0;
		} else if(p%n==1) {
				a[p/n][0]=0;
		} else {
				a[p/n][(p%n)-1]=0;
				long i=p/n;
				long j=(p%n)-1;
				long m[5]={i,n-1-i,j,n-1-j};
				for(int jj=0;jj<i;jj++) {
					if(a[jj][j]==0) {
						m[0]--;
					}
				}
				for(int jj=n-1;jj>i;jj--) {
					if(a[jj][j]==0) {
						m[1]--;
					}
				}
				for(int jj=0;jj<j;jj++) {
					if(a[i][jj]==0) {
						m[2]--;
						}
				}
				for(int jj=n-1;jj>j;jj--) {
					if(a[i][jj]==0) {
						m[3]--;
												}
				}
				qsort(m,4,sizeof(long),compare_int);
				long mm=m[0];
				cnt=cnt+mm;
			}
		}
	printf("%ld\n",cnt);
	return 0;
}