import java.util.*;
import java.io.*;
public class Solution
{
  public static ArrayList<ArrayList<Integer>> table;
  public static void main(String [] args)
  {
    Scanner input = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
    int t = Integer.parseInt(input.nextLine());
    for(int iii = 1; iii <= t; iii++)
    {
      int n = input.nextInt();
      int[] aw = new int[n];
      table = new ArrayList<ArrayList<Integer>>();
      table.add( new ArrayList<Integer>());
      for(int i = 0; i < n; i++)
      {
        aw[i]=input.nextInt();
        table.add( new ArrayList<Integer>());
      }
      for(int i = 1; i <= n; i++)
      {
        table.set(i,recurse(aw,i));
      }
      int max = table.get(n).size();
      for(int i = 0; i < n; i++ )
      {
        table = new ArrayList<ArrayList<Integer>>();
        for(int ii = 0; ii < n; ii++)
        {
          table.add( new ArrayList<Integer>());
        }
        int[] aww = new int[n-1];
        for(int ii = 0; ii < i; ii++ )
        {
          aww[ii]=aw[ii];
        }
        for(int ii = i+1; ii < n; ii++)
        {
          aww[ii-1]=aw[ii];
        }
        for(int ii = 1; ii <= n-1; ii++)
        {
          table.set(ii,recurse(aww,ii));
        }
        int tempmax = table.get(n-1).size();
        if(tempmax>max)
          max=tempmax;
      }
      for(int i = 0; i < n; i++ )
      {
        for(int j = i+1; j < n; j++)
        {
          table = new ArrayList<ArrayList<Integer>>();
          for(int ii = 0; ii < n-1; ii++)
          {
            table.add( new ArrayList<Integer>());
          }
          int[] aww = new int[n-2];
          for(int ii = 0; ii < i; ii++ )
          {
            aww[ii]=aw[ii];
          }
          for(int ii = i+1; ii < j; ii++)
          {
            aww[ii-1]=aw[ii];
          }
          for(int ii = j+1; ii < n; ii++)
          {
            aww[ii-2]=aw[ii];
          }
          for(int ii = 1; ii <= n-2; ii++)
          {
            table.set(ii,recurse(aww,ii));
          }
          int tempmax = table.get(n-2).size();
          if(tempmax>max)
            max=tempmax;
        }
      }
      System.out.println("Case #"+iii+": "+max);
    }
  }
  public static ArrayList<Integer> recurse(int[] aw, int n)
  {
    ArrayList<Integer> resul = new ArrayList<Integer>();
    if(n==1){resul.add(0);}
    else
    {
      int maxlength = -1;
      int minweight = 100000000;
      int goodindex = -1;
      boolean addon = false;
      for(int i = 0; i < n; i++)
      {
        boolean tempaddon = false;
        ArrayList<Integer> result = table.get(i);
        int leng = result.size();
        if (leng < maxlength) continue;
        int weight = 0;
        for(int ii : result)
        {
          weight += aw[ii];
        }
        if(weight<=6*aw[n-1]){leng ++;weight += aw[n-1];tempaddon=true;}
        if(maxlength==leng){if(weight<minweight){minweight=weight;goodindex=i;addon=tempaddon;}}else{maxlength=leng; minweight=weight; goodindex=i;addon=tempaddon;}
      }
      for(int i : table.get(goodindex))
      {
        resul.add(i);
      }
      if(addon)resul.add(n-1);
    }
    return resul;
  }
}