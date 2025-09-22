#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define lli long long int
#define BIG 1000000007
void debug_c(char **dp, int h, int w)
{
	printf("----debug\n");
	int i = 0;
	int j = 0;
	while (i < h)
	{
		j = 0;
		while (j < w)
		{
			printf("%d,",dp[i][j]);
			j++;
		}
		printf("\n");
		i++;
	}
	printf("----debug\n");
}
void debug(int **dp, int h, int w)
{
	printf("----debug\n");
	int i = 0;
	int j = 0;
	while (i < h)
	{
		j = 0;
		while (j < w)
		{
			printf("%d",dp[j][i]);
			j++;
		}
		printf("\n");
		i++;
	}
	printf("----debug\n");
}
int main(void)
{	
	int h, w;
	scanf("%d %d", &h, &w);
	int i = 0;
	int j = 0;
	char **a;
	int **dp;
	a = (char **)malloc(sizeof(char *)*(h));
	dp = (int **)malloc(sizeof(int *)*(w));
	while (i < w)
	{
		dp[i] = (int *)malloc(sizeof(int)*(h));
		i++;
	}
	while (j < h)
	{
		a[j] = (char *)malloc(sizeof(char)*(w));
		j++;
	}
	i = 0;
	j = 0;
	while (i < h)
	{
		j = 0;
		scanf("%s",a[i]);
		while (j < w)
		{
			dp[j][i] = 0;
			if(a[i][j] == '#')
			{
				dp[j][i] = -1;
			}
			j++;
		}
		i++;
	}
	dp[0][0] = 1;
	i = 1;
	j = 1;
	while (i < h)
	{
		if(dp[0][i] == -1)
		{
			dp[0][i] = 0;
		}
		else
		{
			dp[0][i] = dp[0][i-1];
		}
		i++;
	}
	while (j < w)
	{
		if(dp[j][0] == -1)
		{
			dp[j][0] = 0;
		}
		else
		{
			dp[j][0] = dp[j-1][0];
		}
		j++;
	}
	i = 1;
	j = 1;
	while (i< h)
	{
		j = 1;
		while (j < w)
		{
			if(dp[j][i] == -1)
			{
				dp[j][i] = 0;
			}
			else
			{
				dp[j][i] = (dp[j-1][i]+dp[j][i-1])%BIG;
			}
			j++;
		}
		i++;
	}
	printf("%d\n",dp[w-1][h-1]);
	return (0);
}