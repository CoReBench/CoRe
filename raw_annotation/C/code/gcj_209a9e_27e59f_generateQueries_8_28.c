#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<ctype.h>
int sol[151];
int queryList[150];
char solStr[151];
int generateQueries(int n)
{
    int beginning = 1, end = n, i = 0;
    while(beginning <= end)
    {
        queryList[i] = beginning;
        beginning++;
        i++;
        if(beginning < end)
        {
            queryList[i] = end;
            end--;
            i++;
        }
    }
    while(i < 150)
    {
        queryList[i] = -1;
        i++;
    }
}
int findFlipBit(int n)
{
    int i = 1;
    while(i <= n && sol[i] != 2)
    {
        if(sol[i] == sol[n-i+1])
        {
            return i;
        }
        else i++;
    }
    return -1;
}
int findSwapBit(int n)
{
    int i = 1;
    while(i <= n && sol[i] != 2 && sol[n-i+1] != 2)
    {
        if(sol[i] != sol[n-i+1])
        {
            return i;
        }
        else i++;
    }
    return -1;
}
int query(int i)
{
    int ret;
    printf("%d\n", i);
    fflush(stdout);
    scanf("%d", &ret);
    if(ret == 'N')
    {
        exit(1);
    }
    else
    {
        return ret;
    }
}
void flipSol(int n)
{
    for(int i = 1; i <= n; i++)
    {
        if(sol[i] == 1) sol[i] = 0;
        else if(sol[i] == 0) sol[i] = 1;
    }
}
void swapSol(int n)
{
    int beginning = 1, end = n;
    while (beginning < end)
    {
        int aux = sol[beginning];
        sol[beginning] = sol[end];
        sol[end] = aux;
        beginning++;
        end--;
    }
}
void resolve(int n)
{
    for(int i = 1; i <= n; i++)
    {
        sol[i] = 2;
    }
    generateQueries(n);
    int queries = 0;
    int known = 0;
    int flipBit = -1, swapBit = -1;
    int flipRes, swapRes, doubleRes;
    bool flipped = false, swapped = false;
    while(true)
    {
        if(queries % 10 == 0 && queries != 0)
        {
            if(flipBit == -1) flipBit = findFlipBit(n);
            if(flipBit != -1)
            {
                flipRes = query(flipBit);
                if(flipRes != sol[flipBit]) flipSol(n);
                else flipped = false;
                queries++;
            }
            else
            {
                query(1);
                queries++;
            }
            if(swapBit == -1)
            {
                swapBit = findSwapBit(n);
            }
            if(swapBit != -1)
            {
                swapRes = query(swapBit);
                if(swapRes != sol[swapBit]) swapSol(n);
                else swapped = false;
                queries++;
            }
            else
            {
                query(1);
                queries++;
            }
        }
        else
        {
            sol[queryList[known]] = query(queryList[known]);
            known++;
            queries++;
            if(queryList[known] == -1)
            {
                for(int i = 1; i < n; i++)
                {
                    printf("%d", sol[i]);
                }
                printf("%d\n", sol[n]);
                fflush(stdout);
                char answer  = 10;
                while (answer == 10)
                {
                    answer = getchar();
                }
                if(answer == 'Y')
                {
                    return;
                }
                else
                {
                    exit(7);
                }
            }
        }
    }
}
int main(void)
{
    int t, n;
    scanf("%d %d", &t, &n);
    for(int test = 0; test < t; test++)
    {
        resolve(n);
    }
    return 0;
}