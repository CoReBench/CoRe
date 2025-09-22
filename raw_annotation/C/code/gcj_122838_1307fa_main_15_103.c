#include <stdio.h>
#include <stdlib.h>
int min(int a, int b){
	if(a>b){
		return b;
	}
	return a;
}
int max(int a, int b){
	if(a>b){
		return a;
	}
	return b;
}
int main(){
	int t;
	scanf("%d",&t);
	for (int m = 1; m <= t; ++m)
	{
		int n,k;
		scanf("%d%d",&n,&k);
		int a[n],b[n],l_a[n],l_b[n],r_a[n],r_b[n];
		for (int i = 0; i < n; ++i)
		{
			l_a[i]=l_b[i]=r_a[i]=r_b[i] = i;
		}
		for (int i = 0; i < n; ++i)
		{
			scanf("%d",a+i);
		}
		for (int i = 0; i < n; ++i)
		{
			scanf("%d",b+i);
		}
		for (int i = 0; i < n; ++i)
		{
			int l_temp = i;
			while(l_temp>-1){
				if(a[l_temp]<=a[i]){
					l_temp--;
				}
				else{
					break;
				}
			}
			l_a[i] = l_temp;
			l_temp = i;
			while(l_temp>-1){
				if(b[l_temp]<=b[i]){
					l_temp--;
				}
				else{
					break;
				}
			}
			l_b[i] = l_temp;
			l_temp = i;
			while(l_temp<n){
				if(a[l_temp]<=a[i]){
					l_temp++;
				}
				else{
					break;
				}
			}
			r_a[i] = l_temp;
			l_temp = i;
			while(l_temp<n){
				if(b[l_temp]<=b[i]){
					l_temp++;
				}
				else{
					break;
				}
			}
			r_b[i] = l_temp;
		}
		long long int tot = 0;
		for (int i = 0; i < n; ++i)
		{
			for (int j = i; j < r_a[i]; ++j)
			{
				if(l_b[j] < i){
					if(a[i]-b[j] <= k && a[i]-b[j] >= -k){
						tot += (i-max(l_a[i],l_b[j]))*(min(r_a[i],r_b[j])-j);
					}
				}
			}
		}
		for (int i = 0; i < n; ++i)
		{
			for (int j = i+1; j < r_b[i]; ++j)
			{
				if(l_a[j] < i){
					if(a[j]-b[i] <= k && a[j]-b[i] >= -k){
						tot += (i-max(l_b[i],l_a[j]))*(min(r_b[i],r_a[j])-j);
					}
				}
			}
		}
		printf("Case #%d: %lld\n", m,tot);
	}
}