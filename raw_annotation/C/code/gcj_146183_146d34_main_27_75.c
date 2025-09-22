#include <stdio.h>
#include <stdlib.h>
typedef struct st
{
    int x;
    int y;
}arr;
arr array[100005];
int comp(const void *a, const void *b)
{
    long long int c1 = (*(arr*)a).x;
    c1 *= (*(arr*)b).y;
    long long int c2 = (*(arr*)b).x;
    c2 *= (*(arr*)a).y;
    if (c1 == c2) return 0;
    else if (c1 > c2) return 1;
    else return -1;
}
int abs(int n)
{
    if (n < 0)
    {
        return -1 * n;
    }
    return n;
}
int main()
{
    int input[310][2];
    int cases, N;
    scanf("%d", &cases);
    for (int cas = 1; cas <= cases; cas++)
    {
        scanf("%d", &N);
        for (int i = 1; i <= N; i++)
        {
            scanf("%d %d", &input[i][0], &input[i][1]);
        }
        int pair = 0;
        for (int i = 1; i <= N; i++)
        {
            for (int j = i + 1; j <= N; j++)
            {
                long long int tmp = input[i][0] - input[j][0];
                tmp *= input[i][1] - input[j][1];
                if (tmp < 0)
                {
                    array[pair].x = abs(input[i][0] - input[j][0]);
                    array[pair].y = abs(input[i][1] - input[j][1]);
                    pair++;
                }
            }
        }
        if (pair == 0)
        {
            printf("Case #%d: 1\n", cas);
        }
        else
        {
            qsort(array, pair, sizeof(arr), comp);
            int ans = 2;
            for (int i = 1; i < pair; i++)
            {
                long long int c1 = array[i - 1].x * array[i].y;
                long long int c2 = array[i - 1].y * array[i].x;
                if (c1 != c2)
                {
                    ans++;
                }
            }
            printf("Case #%d: %d\n", cas, ans);
        }
    }
    return 0;
}