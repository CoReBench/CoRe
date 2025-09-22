#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
typedef struct
{
	int x;
	int y;
} par;
double get_double();
int get_int();
int max(int, int);
int min(int, int);
int main()
{
	int i, j, k;
	int t = get_int();
	for (i = 0; i < t; i++)
	{
		int n = get_int();
		int w[n];
		int c[n][n];
		memset(c, 0, sizeof(c));
		for (j = 0; j < n; j++)
		{
			w[j] = get_int();
		}
		c[0][0] = w[0];
		for (j = 1; j < n; j++)
		{
			c[0][j] = min(w[j], c[0][j - 1]);
		}
		for (j = 1; j < n; j++)
		{
			if (c[j - 1][j - 1] == -1)
			{
				c[j][j] = -1;
			}
			else
			{
				if (c[j - 1][j - 1] > w[j]*6)
				{
					c[j][j] = -1;
				}
				else
				{
					c[j][j] = c[j - 1][j - 1] + w[j];
				}
			}
		}
		for (j = 1; j < n; j++)
		{
			for (k = j + 1; k < n; k++)
			{
				if (c[j - 1][k - 1] == -1 && c[j][k - 1] == -1)
				{
					c[j][k] = -1;
				}
				else if (c[j - 1][k - 1] == -1)
				{
					if (c[j][k - 1] > w[k]*6)
					{
						c[j][k] == -1;
					}
					else
					{
						c[j][k] = c[j][k - 1] + w[k];
					}
				}
				else if(c[j][k - 1] == -1)
				{
					if (c[j - 1][k - 1] > w[k]*6)
					{
						c[j][k] == -1;
					}
					else
					{
						c[j][k] = c[j - 1][k - 1] + w[k];
					}
				}
				else
				{
					int tmp = min(c[j - 1][k - 1], c[j][k - 1]);
					if (tmp > w[k]*6)
					{
						c[j][k] = -1;
					}
					else
					{
						c[j][k] = tmp + w[k];
					}
				}
			}
		}
		for (j = 0; j < n; j++)
		{
			if (c[j][n - 1] == -1)
			{
				break;
			}
		}
		printf("Case #%d: %d\n", i + 1, j);
	}
}
int max(int a, int b)
{
	if (a > b)
	{
		return a;
	}
	return b;
}
int min(int a, int b)
{
	if (a < b)
	{
		return a;
	}
	return b;
}
double get_double()
{
	double ret = 0;
	char c     = getchar();
	int sgn;
	while (1)
	{
		if (c == EOF)
		{
			return EOF;
		}
		if (c >= '0' && c <= '9')
		{
			sgn = 1;
			break;
		}
		if (c == '-')
		{
			c = getchar();
			if (c < '0' || c > '9')
			{
				continue;
			}
			sgn = -1;
			break;
		}
		c = getchar();
	}
	while (1)
	{
		ret = ret*10 + c - '0';
		c = getchar();
		if (c == '.')
		{
			double pos = 0.1;
			c = getchar();
			while (c >= '0' && c <= '9')
			{
				ret += pos*(c - '0');
				pos /= 10;
				c = getchar();
			}
			return sgn*ret;
		}
		else if (c < '0' || c > '9')
		{
			return sgn*ret;
		}
	}
}
int get_int()
{
	int ret = 0;
	char c  = getchar();
	int sgn;
	while (1)
	{
		if (c == EOF)
		{
			return EOF;
		}
		if (c >= '0' && c <= '9')
		{
			sgn = 1;
			break;
		}
		if (c == '-')
		{
			c = getchar();
			if (c < '0' || c > '9')
			{
				continue;
			}
			sgn = -1;
			break;
		}
		c = getchar();
	}
	while (1)
	{
		ret = (ret << 3) + (ret << 1) + c - '0';
		c = getchar();
		if (c < '0' || c > '9')
		{
			return sgn*ret;
		}
	}
}