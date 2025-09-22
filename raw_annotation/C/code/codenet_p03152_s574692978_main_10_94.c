#include<stdio.h>
#include<math.h>
int min(int a, int b)
{
    if (a < b)
        return a;
    else
        return b;
}
int main()
{
    int n, m;
    scanf("%d %d", &n, &m);
    int a[1003], b[1003];
    int i;
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);
    for (i = 0; i < m; i++)
        scanf("%d", &b[i]);
    int x;
    for(i=0;i<n-1;i++)
        if (a[i] <= a[i + 1])
        {
            if (a[i] == a[i + 1])
            {
                printf("0\n");
                return 0;
            }
            x = a[i];
            a[i] = a[i + 1];
            a[i + 1] = x;
            if (i > 0)
                i -= 2;
        }
    for(i=0;i<m-1;i++)
        if (b[i] <= b[i + 1])
        {
            if (b[i] == b[i + 1])
            {
                printf("0\n");
                return 0;
            }
            x = b[i];
            b[i] = b[i + 1];
            b[i + 1] = x;
            if (i > 0)
                i -= 2;
        }
    int p = 1000000007;
    double ans = 1;
    int k = 0;
    int y;
    int j;
    int q;
    for (i = n * m; i >= min(a[n - 1], b[m - 1]); i--)
    {
        x = y = q = 0;
        j = 0;
        while (a[j] > i)
        {
            j++;
            x++;
        }
        if (a[j] == i)
        {
            x = 1;
            q++;
        }
        j = 0;
        while (b[j] > i)
        {
            y++;
            j++;
        }
        if (b[j] == i)
        {
            y = 1;
            q++;
        }
        if (q==0)
            ans *= x * y - k;
        else
            ans *= x * y;
        ans = round(fmod(ans, p));
        k++;
    }
    for (j = 0; j < i; j++)
    {
        ans *= j + 1;
        ans = round(fmod(ans, p));
    }
    printf("%.0lf\n", round(ans));
    return 0;
}