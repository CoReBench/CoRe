#include <stdio.h>
#include <string.h>
int abs(int x)
{
	if(x < 0)
		return -x;
	else
		return x;
}
int main(void)
{
	int n;
	int a[100000];
	int i, j;
	int sum = 0;
	int ans = 0;
	char sign;
	scanf("%d", &n);
	for(i=0; i<n; i++)
		scanf("%d", &a[i]);
	for(i=0; i<n; i++){
		if(a[i] > 0){
			sign = 'p';
			break;
		}
		else if(a[i] < 0){
			sign = 'm';
			break;
		}
		else
			continue;
	}
	for(; i<n; i++){
		sum += a[i];
		if(sum == 0){
			for(j=i+1; j<n; j++){
				if(sum == a[j])
					continue;
				else if(sign == 'p'){
					sum++;
					ans++;
					i = j;
					break;
				}
				else if(sign == 'm'){
					sum--;
					ans++;
					i = j;
					break;
				}
			}
			i = j;
			ans++;
		}
		else if(sum > 0 && sign == 'p')
			sign = 'm';
		else if(sum < 0 && sign == 'm')
			sign = 'p';
		else{
			if(sign == 'p'){
				ans += abs(sum)+1;
				sum += abs(sum)+1;
				sign = 'm';
			}
			else if(sign == 'm'){
				ans += abs(sum)+1;
				sum -= abs(sum)+1;
				sign = 'p';
			}
		}
	}
	printf("%d\n", ans);
	return 0;
}