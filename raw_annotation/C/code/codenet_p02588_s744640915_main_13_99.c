#include<stdio.h>
long long int gcd(long long int a, long long int b)
{
	long long int r = a % b;
	while (r > 0)
	{
		a = b;
		b = r;
		r = a % b;
	}
	return b;
}
int main()
{
	long long int n;
	scanf("%lld", &n);
	long long int i, j, k;
	char s[100];
	long long int a[200005];
	for (i = 0; i < n; i++)
	{
		scanf("%s", s);
		a[i] = 0;
		k = 0;
		for (j = 0; s[j] != '\0'; j++)
		{
			if (s[j] != '.')
			{
				a[i] = 10 * a[i] + (long long int)(s[j] - '0');
				if (k > 0)
					k++;
			}
			else
				k = 1;
		}
		if (k == 0)
			k = 1;
		for (; k < 10; k++)
			a[i] *= 10;
	}
	long long int q = 100000;
	for (i = 0; i < n; i++)
	{
		if (a[i] % q > 0)
			a[i] = -1;
		else
			a[i] = a[i] / q;
	}
	q = 100000000;
	long long int b[10004];
	j = 0;
	for (i = 1; i * i <= q; i++)
	{
		if (q % i == 0)
		{
			b[j] = i;
			j++;
		}
	}
	i--;
	if (i * i == q)
		i--;
	for (; i > 0; i--)
	{
		if (q % i == 0)
		{
			b[j] = q / i;
			j++;
		}
	}
	long long int min, mid, max;
	long long int c[10004];
	for (i = 0; i < j; i++)
		c[i] = 0;
	long long int ans = 0;
	long long int l;
	for (i = 0; i < n; i++)
	{
		if (a[i] < 0)
			continue;
		l = q / gcd(q, a[i]);
		min = -1;
		max = j;
		while (max - min > 1)
		{
			mid = (max + min) / 2;
			if (b[mid] < l)
				min = mid;
			else
				max = mid;
		}
		ans += c[max];
		for (k = 0; k < j; k++)
			if (a[i] % b[k] == 0)
				c[k]++;
	}
	printf("%lld\n", ans);
	return 0;
}