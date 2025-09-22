#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
#include<stdbool.h>
#include<stdlib.h>
#include<math.h>
#include<malloc.h>
void CodeJam(int n)
{
	int i, j, k;
	k = 0;
	char tmp[1000][51];
	char word[1000][51];
	char rw[1000][51];
	int match[1000] = { 0, };
	int max[1000] = { 0, };
	for (i = 0; i != n; i++)
	{
		scanf("%s", word[i]);
	}
	for (i = 0; i != 1000; i++)
	{
		for (j = 0; j != 50; j++)
		{
			rw[i][j] = word[i][j];
		}
	}
	for (i = 0; i != n; i++)
	{
		for (j = 0; j != strlen(word[i]); j++)
		{
			rw[i][j] = word[i][strlen(word[i]) - j - 1];
		}
	}
	for (i = 0; i != n - 1; i++)
	{
		for (j = 0; j != n - 1 - i; j++)
		{
			if (strcmp(word[j], word[j + 1]) > 0)
			{
				strcpy(tmp[j], word[j]);
				strcpy(word[j], word[j + 1]);
				strcpy(word[j + 1], tmp[j]);
			}
		}
	}
	for (i = 0; i != n - 1; i++)
	{
		for (j = 0; j != strlen(rw[i]) > strlen(rw[i + 1]) ? strlen(rw[i + 1]) : strlen(rw[i]); j++)
		{
			if (rw[i][j] == rw[i + 1][j])
			{
				match[i]++;
			}
			else
			{
				break;
			}
		}
	}
	max[0] = match[0];
	max[1] = match[1];
	for (i = 2; i != 1000; i++)
	{
		max[i] = max[i - 2] + match[i];
	}
	printf("%d\n", max[999] > max[998] ? max[999] : max[998]);
}
int main()
{
	int i;
	int t;
	scanf("%d", &t);
	for (i = 1; i <= t; ++i)
	{
		printf("Case #%d: ", i);
		int N;
		scanf("%d", &N);
		CodeJam(N);
	}
	return 0;
}