import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
public class Main {
  public static void main(String[] args) {
    new Main().run();
  }
  public void run() {
    try(BufferedReader in = new BufferedReader(new InputStreamReader(System.in))) {
      int n = Integer.parseInt(in.readLine());
      String line = in.readLine();
      int[] seqA = new int[n/2];
      int[] seqB = new int[n/2];
      int offset=0,next=0;
      char regx = ' ';
      List<Integer> listA = new ArrayList<>();
      List<Integer> listB = new ArrayList<>();
      Map<Integer,Integer> mapA = new HashMap<>();
      Map<Integer,Integer> mapB = new HashMap<>();
      for(int i=0, j=0; i<n; i++, j= i >> 1) {
        if((next = line.indexOf(regx,offset)) == -1)
          next = line.length();
        if((i & 1) == 0) {
          seqA[j] = Integer.parseInt(line.substring(offset, next));
          if(mapA.containsKey(seqA[j])) {
            mapA.replace(seqA[j], mapA.get(seqA[j]) + 1);
          } else {
            mapA.put(seqA[j], Integer.valueOf(1));
            listA.add(seqA[j]);
          }
        }
        else {
          seqB[j] = Integer.parseInt(line.substring(offset, next));
          if(mapB.containsKey(seqB[j])) {
            mapB.replace(seqB[j], mapB.get(seqB[j]) + 1);
          } else {
            mapB.put(seqB[j], Integer.valueOf(1));
            listB.add(seqB[j]);
          }
        }
        offset = ++next;
      }
      int vma,vmb,xa,xb;
      vma = vmb = xa = xb =0;
      for (Integer var : listA) {
        if(vma < mapA.get(var)) {
          vma = mapA.get(var);
          xa = var;
        }
      }
      for (Integer var : listB) {
        if(vmb < mapB.get(var)) {
          vmb = mapB.get(var);
          xb = var;
        }
      }
      int cca,ccb;
      cca = ccb = 0;
      for (int i : seqA) {
        if(i != xa) cca++;
      }
      for (int i : seqB) {
        if(i != xb) ccb++;
      }
      int vma2,vmb2,xa2,xb2;
      vma2 = vmb2= xa2 = xb2 =0;
      int cca2,ccb2;
      cca2 = ccb2 = 0;
      int ans = 0;
      if(xa == xb) {
        for (Integer var : listA) {
          int ma = mapA.get(var);
          if(var != xa && vma2 < ma) {
            vma2 = ma;
            xa2 = var;
          }
        }
        for (Integer var : listB) {
          int mb = mapB.get(var);
          if(var != xb && vmb2 < mb) {
            vmb2 = mb;
            xb2 = var;
          }
        }
        for (int i : seqA) {
          if(i != xa2) 
            cca2++;
        }
        for (int i : seqB) {
          if(i != xb2) 
            ccb2++;
        }
        ans = cca2 > ccb2 ? cca + ccb2 : cca2 + ccb;
      }
      else {
        ans = cca + ccb;
      }
      System.out.println(ans);
    }
    catch(IOException e) {
      System.err.println(e);
    }
  }
}