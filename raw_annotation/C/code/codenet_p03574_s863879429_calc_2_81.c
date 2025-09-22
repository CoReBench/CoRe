#include <stdio.h>
int calc(h, w)
{
    int panel[h][w];
    char row[w];
    for (int i = 0; i < h; i++)
    {
        scanf("%s", row);
        for (int j = 0; j < w; j++)
        {
            if (row[j] == '#')
            {
                panel[i][j] = -1;
            }
            else
            {
                panel[i][j] = 0;
            }
        }
    }
    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            if (panel[i][j] == -1)
            {
                continue;
            }
            int count = 0;
            if (0 <= (i - 1) && 0 <= (j - 1) && panel[i - 1][j - 1] == -1)
            {
                count++;
            }
            if (0 <= (i - 1) && panel[i - 1][j] == -1)
            {
                count++;
            }
            if (0 <= (i - 1) && (j + 1) < w && panel[i - 1][j + 1] == -1)
            {
                count++;
            }
            if (0 <= (j - 1) && panel[i][j - 1] == -1)
            {
                count++;
            }
            if ((j + 1) < w && panel[i][j + 1] == -1)
            {
                count++;
            }
            if ((i + 1) < h && 0 <= (j - 1) && panel[i + 1][j - 1] == -1)
            {
                count++;
            }
            if ((i + 1) < h && panel[i + 1][j] == -1)
            {
                count++;
            }
            if ((i + 1) < h && (j + 1) < w && panel[i + 1][j + 1] == -1)
            {
                count++;
            }
            panel[i][j] = count;
        }
    }
    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            if (panel[i][j] == -1)
            {
                printf("#");
            }
            else
            {
                printf("%d", panel[i][j]);
            }
        }
        printf("\n");
    }
    return 0;
}
int main()
{
    int h, w;
    scanf("%d %d", &h, &w);
    calc(h, w);
    return 0;
}