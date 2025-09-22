#include <stdio.h>
#include <string.h>
#define max(a,b) ((a)>=(b)?(a):(b))
int dp[3001][3001];
char buf[30], *p;
int getint()
{
	int n = 0;
	while (*p >= '0') n = (n<<3) + (n<<1) + (*p++ & 0xf);
	return n;
}
int main()
{	
	int a[3001];
	int b[3001];
	int n, t, s, i, j, k, ans;
	fgets(p=buf, 30, stdin);
	n = getint();
	p++;
	t = getint();
	p++;
	s = getint();
	for (i = 1; i <= n; i++) {
		fgets(p=buf, 30, stdin);
		a[i] = getint();
		p++;
		b[i] = getint();
	}
	ans = 0;
	for (i = 1; i <= n; i++) 
		for (j = 1; j <= t; j++) {
			dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
			k = j-b[i];
			if (k >= 0 && (s <= k || j <= s))
				dp[i][j] = max(dp[i][j], dp[i-1][k] + a[i]);
			ans = max(ans, dp[i][j]);
		}
	printf("%d\n", ans);
	return 0;
}