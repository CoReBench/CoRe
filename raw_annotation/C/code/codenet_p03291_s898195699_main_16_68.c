#include<stdio.h>
#include<string.h>
long long int modpow(long long int a, long long int n, long long int p)
{
	if (n < 0)return 0;
	long long int res = 1;
	while (n > 0)
	{
		if (n % 2 == 1)
			res = res * a % p;
		a = a * a % p;
		n /= 2;
	}
	return res;
}
int main()
{
	char s[100005];
	scanf("%s", s);
	long long int i, n = strlen(s);
	long long int ca[100005], cha[100005];
	ca[0] = cha[0] = 0;
	for (i = 0; i < n; i++)
	{
		if (s[i] == 'A')
		{
			ca[i + 1] = ca[i] + 1;
			cha[i + 1] = cha[i];
		}
		else if (s[i] == '?')
		{
			ca[i + 1] = ca[i];
			cha[i + 1] = cha[i] + 1;
		}
		else
		{
			ca[i + 1] = ca[i];
			cha[i + 1] = cha[i];
		}
	}
	long long int cc[100005], chc[100005];
	cc[n] = chc[n] = 0;
	for (i = n - 1; i >= 0; i--)
	{
		if (s[i] == 'C')
		{
			cc[i] = cc[i + 1] + 1;
			chc[i] = chc[i + 1];
		}
		else if (s[i] == '?')
		{
			cc[i] = cc[i + 1];
			chc[i] = chc[i + 1] + 1;
		}
		else
		{
			cc[i] = cc[i + 1];
			chc[i] = chc[i + 1];
		}
	}
	long long int p = 1000000007;
	long long int ans = 0;
	for (i = 0; i < n; i++)
		if (s[i] == 'B' || s[i] == '?')
			ans = (ans + ((ca[i] * modpow(3, cha[i], p) % p + cha[i] * modpow(3, cha[i] - 1, p) % p) % p) * ((cc[i + 1] * modpow(3, chc[i + 1], p) % p + chc[i + 1] * modpow(3, chc[i + 1] - 1, p) % p) % p)) % p;
	printf("%lld\n", ans);
	return 0;
}