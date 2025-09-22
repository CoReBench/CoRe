#include <stdio.h>
int len(char s[1001])
{ 
    int i;
    for(i=0;s[i]!='\0';i++);
    return i;
}
int main(void) {
	int t=0,n=0,i,j,k; char s[10001],str[101];
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
	    scanf("%d",&n);
	    char a[n][10001],dd;
	    for(j=0;j<n;j++)
	    for(k=0;k<10001;k++)
	    a[j][k]='#'; 
		int flag=0;
	    for(j=0;j<n;j++)
	    {
	        scanf("%c",&dd);
	        scanf("%s",str);
	        if(str[0]=='*')
	        {
	            int x=10000;
	            for(k=len(str);k>=0;k--) { 
					a[j][x--]=str[k]; 
				}
	        }
	        else if(str[len(str)-1]=='*')
	        {
	            for(k=0;str[k]!='\0';k++)
	            	a[j][k]=str[k];
	        }
	    }
	    int x=0;
	    for(j=0;j<10000;j++)
	    {
	        int f=0;
	        for(k=0;k<n;k++)
	        {
	            if(f==1&&a[k][j]!=s[x-1]&&a[k][j]!='*'&&a[k][j]!='#'){
					flag=1; 
					break; 
				}
	            else if(a[k][j]!='*'&&a[k][j]!='#') { 
					if(f==0) {
						s[x++]=a[k][j]; 
						f=1;
					} 
				}
	        }
	        if(flag==1) 
				break;
	    }
	    s[x]='\0';
	    if(flag==1) 
			printf("Case #%d: *\n",i);
	    else 
			printf("Case #%d: %s\n",i,s);
	}
	return 0;
}