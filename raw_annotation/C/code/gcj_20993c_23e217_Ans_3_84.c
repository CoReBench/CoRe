#include <stdio.h>
#include <math.h>
int Ans(long long int x)
{
    long long int n,i,j,sum=0,r,c,k;
    scanf("%lld",&n);
    long long int Mat[n][n],count[n];
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
            scanf("%lld",&Mat[i][j]);
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            if(i==j)
            {
                sum=sum+Mat[i][j];
            }
        }
    }
    for(i=0;i<n;i++)
    {
        count[i]=0;
        for(j=0; j<n; j++)
        {
            for(k=j+1; k<n; k++)
            {
                if(Mat[i][j] == Mat[i][k])
                {
                	if(count[i]==0)
                		count[i]=count[i]+2;
                	else
                    	count[i]++;
                    break;
                }
            }
        }
    }
    long long int rmax=count[0];
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            if(count[j]>=count[j+1])
            {
                rmax=count[j];
            }
        }
    }
    long long int ccount[n];
    for(j=0;j<n;j++)
    {
        ccount[j]=0;
        for(i=0; i<n; i++)
        {
            for(k=i+1; k<n; k++)
            {
                if(Mat[i][j] == Mat[k][j] )
                {
                	if(ccount[j]==0)
                		ccount[j]=ccount[j]+2;
                	else
                    	ccount[j]++;
                    break;
                }
            }
        }
    }
    long long int cmax=ccount[0];
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            if(ccount[j]>=ccount[j+1])
            {
                cmax=ccount[j];
            }
        }
    }
    printf("Case #%lld: %lld %lld %lld\n",x+1,sum,rmax,cmax);
    return 0;
}
int main()
{
    long long int i,T;
    scanf("%lld",&T);
    for(i=0;i<T;i++)
        Ans(i);
    return 0;
}