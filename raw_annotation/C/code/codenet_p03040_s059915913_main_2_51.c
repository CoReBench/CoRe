#include<stdio.h>
int main()
{
	int q;
	scanf("%d", &q);
	int n = 0;
	long long int a[200005], b = 0;
	long long int x, y, z;
	int i, j;
	long long int m;
	long long int ans;
	for (i = 0; i < q; i++)
	{
		scanf("%lld", &x);
		if (x == 1)
		{
			scanf("%lld %lld", &y, &z);
			if (n == 0)
				a[0] = y;
			else
			{
				for (j = n - 1; j >= 0; j--)
				{
					if (a[j] > y)
						a[j + 1] = a[j];
					else
					{
						a[j + 1] = y;
						break;
					}
					if (j == 0)
						a[0] = y;
				}
			}
			n++;
			b += z;
		}
		else
		{
			m = a[(n - 1) / 2];
			ans = b;
			for (j = 0; j < n; j++)
				if (m - a[j] < 0)
					ans += - (m - a[j]);
				else
					ans += m - a[j];
			printf("%lld %lld\n", m, ans);
		}
	}
	return 0;
}