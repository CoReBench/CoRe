#include <stdio.h>
#include <string.h>
void MakeCostMinimum(int p, int q, int r)
{
    int minimumcost = (q - p) + (r - q);
    if (minimumcost < 0)
        minimumcost = minimumcost * (-1);
    else
        ;
    printf("%d\n", minimumcost);
}
void Compare3Figures(int a, int b, int c)
{
    if (b < a && a < c)
    {
        int tmp = a;
        a = b;
        b = tmp;
    }
    else if (b < a && c < b)
    {
        int tmptwo = a;
        a = c;
        c = tmptwo;
    }
    else if (a < b && c < b && a < c)
    {
        int tmpthree = b;
        b = c;
        c = tmpthree;
    }
    else if (a < b && c < a)
    {
        int tmpfour = a;
        a = c;
        c = b;
        b = tmpfour;
    }
    else if (b < a && b < c && c < a)
    {
        int tmpfive = a;
        a = b;
        b = c;
        c = tmpfive;
    }
    MakeCostMinimum(a, b, c);
}
int main(int argc, char *argv[])
{
    int A = 0;
    int B = 0;
    int C = 0;
    do
    {
        scanf("%d", &A);
    } while (A < 1 || 100 < A);
    do
    {
        scanf("%d", &B);
    } while (B < 1 || 100 < B);
    do
    {
        scanf("%d", &C);
    } while (C < 1 || 100 < C);
    Compare3Figures(A, B, C);
}