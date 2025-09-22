import java.util.*;
import java.util.ArrayList;
public class Main
{
    public static void main(String args[])
    {
        Scanner in=new Scanner(System.in);
        int t=in.nextInt();
        while(t-->0)
        {
            int n=in.nextInt();
            int a[][]=new int[n][n];
            for(int i=0;i<n;i++)
            {
                for(int j=0;j<n;j++)
                {
                    a[i][j]=in.nextInt();
                }
            }
            vestigium(a,n);
        }
    }
    public static void vestigium(int a[][],int n)
    {
          int k=0;
          int r=0;
          int c=0;
          int b[][]=new int[n][n];
          for(int i=0;i<n;i++)
          {
              k+=a[i][i];
          }
          for(int i=0;i<n;i++)
           {
            for(int j=0;j<n;j++)
            {
               b[i][j]=a[j][i];
            }
           }
           for(int i=0;i<n;i++)
           {
               Arrays.sort(a[i]);
           }
           int repeat=0;
           int count=0;
           for(int i=0;i<n;i++)
           {
               for(int j=0;j<n-1;j++)
               {
                   if(a[i][j]==a[i][j+1])
                   {
                       repeat++;
                   }
                   count=Math.max(count,repeat);
               }
               if(repeat>0)
               {
                   repeat=0;
               }
           }
           for(int i=0;i<n;i++)
           {
            Arrays.sort(b[i]);
           }
          int count1=0;
          int repeat1=0;
             for(int i=0;i<n;i++)
          {
              for(int j=0;j<n-1;j++)
              {
                  if(b[i][j]==b[i][j+1])
                  {
                      repeat1++;
                  }
                  count1=Math.max(count1,repeat1);
              }
              if(repeat1>0)
              {
                  repeat1=0;
              }
          }
         r=count+1;
         c=count1+1;
        int counter=1;
          if(count1==0 && count==0)
          {
              System.out.println("Case #"+counter+": "+" "+k+" "+count+" "+count1);
              counter++;
          }
          else if(count1!=0 && count!=0)
          {
            System.out.println("Case #"+counter+": "+" "+k+" "+r+" "+c);
              counter++;
          }
          else if(count1==0 && count!=0)
          {
            System.out.println("Case #"+counter+": "+" "+k+" "+r+" "+count1);
              counter++;
          }
            else if(count1!=0 && count==0)
          {
            System.out.println("Case #"+counter+": "+" "+k+" "+count+" "+c);
              counter++;
          }
    }
}    