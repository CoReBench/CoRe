#include <stdio.h>
#include <math.h>
int N;
typedef struct _mole {
	int c;
	int j;
}Mole;
Mole arr[305];
int Abs(int a) {
	if (a < 0)
		return -1 * a;
	else
		return a;
}
int gcd(int a, int b) {
	if (b == 0)
		return a;
	else
		return gcd(b, a%b);
}
int main(void) {
	int t, T;
	int i;
	int j;
	int ans;
	int flag;
	double max = -1;
	int ans_c, ans_j;
	int flag_big;
	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		ans = 1;
		scanf("%d", &N);
		for (i = 1; i <= N; i++)
			scanf("%d%d", &arr[i].c, &arr[i].j);
		flag = 0;
		flag_big = -1;
		for (i = 1; i < N; i++) {
			j = i + 1;
			if ((arr[i].c <= arr[j].c && arr[i].j <= arr[j].j))
				continue;
			if (arr[i].c >= arr[j].c && arr[i].j >= arr[j].j) {
				flag = 1;
				break;
			}
			double a = arr[j].c - arr[i].c;
			double b = arr[i].j - arr[j].j; 
			if (flag_big == -1) {
				if (a > 0)
					flag_big = 1;
				else
					flag_big = 0;
			}
			if (flag_big == 1) {
				if (a < 0) {
					flag = 1;
					break;
				}
				if (max < b / a) {
					max = b / a;
				}
			}
			else {
				if (a > 0) {
					flag = 1;
					break;
				}
				if (max < b / a) {
					max = b / a;
				}
			}
		}
		if(flag)
			printf("Case #%d: IMPOSSIBLE\n", t);
		else {
			if (flag_big == -1) {
				ans_c = 1;
				ans_j = 1;
			}
			else if (flag_big == 1) {
				ans_j = 1;
				ans_c = floor(max+1);
			}
			else {
				ans_c = 1;
				ans_j = floor(max + 1);
			}
			printf("Case #%d: %d %d\n", t, ans_c, ans_j);
		}
	}
}