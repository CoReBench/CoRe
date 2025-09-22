#include<stdio.h>
char S[101],str[101];
void check(const char *S)
{
  int i,j;
  int top=0;
  for(i=0;S[i]!='\0';i++)
  {
      if(S[i]=='1')
      {
          str[top]='(';
          ++top;
          str[top]='1';
          ++top;
          str[top]=')';
          ++top;
      }
      else
      {
      str[top]='0';
      ++top;
      }
  }
  str[top]='\0';
  top=0;
  for(i=0;str[i]!='\0';i++)
  {
      if(str[i]==')'&& str[i+1]=='(')
      {
          for(j=i;str[j]!='\0';j++)
          {
              str[j]=str[j+2];
          }
          str[j]='\0';
      }
  }
}
int main(void)
{
  int T,cnt=0;
  scanf("%d",&T);
  while (T!=0)
  {
    scanf("%s\n",S);
    check(S);
    ++cnt;
    printf("Case    #%d:    %s",cnt,str);
    --T;
  }
  return 0;
}