import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;
import java.util.StringTokenizer;
public class Solution {
	int[] array;
    int[] tempMergArr;
    int length;
	public static void main(String[] args) {
		Scanner reader = new Scanner(System.in);  
		int numberOfTests= reader.nextInt();
		int a=0;
		int b=0;
		for(int m=0; m< numberOfTests;m++) { 
			int n  = reader.nextInt();
			if(n%2==1) {
				a=n/2 +1;
				b=n/2;
			}
			else {
				a=n/2;
				b=n/2;
			}
			int[] oddArray = new int[a];
			int[] evenArray = new int[a];
			int c=0;
			int d=0;
			for(int i=0;i<n;i++) {
				if(i%2==0) {
					oddArray[c]=reader.nextInt();
					c++;
				}
				else {
					evenArray[d]=reader.nextInt();
					d++;
				}
			}
			evenArray[evenArray.length-1]=Integer.MAX_VALUE;
			Solution mms = new Solution();
	        mms.sort(oddArray);
	        mms.sort(evenArray);
	        int x=0;
	        for(int h=0;h<oddArray.length;h++) { 
	        	try {
	        		if(oddArray[h]<=evenArray[h]) {
	        			if(h==oddArray.length-1) {
	        				break;
	        			}
	        			if(evenArray[h]<=oddArray[h+1]) {
	        			}
	        			else {
	        				System.out.println("Case #"+(m+1)+": "+(2*h+1));
	        				x++;
	        				break;
	        			}
	        		}
	        		else {
	        			System.out.println("Case #"+(m+1)+": "+2*h);
	        			x++;
	        			break;
	        		}
	        	}
	        	finally {
	        	}
	        }
	        if(x==0) {
	        	System.out.println("Case #"+(m+1)+": OK");
	        }
		}
		reader.close();
	}
	public void sort(int inputArr[]) {
        this.array = inputArr;
        this.length = inputArr.length;
        this.tempMergArr = new int[length];
        doMergeSort(0, length - 1);
    }
    private void doMergeSort(int lowerIndex, int higherIndex) {
        if (lowerIndex < higherIndex) {
            int middle = lowerIndex + (higherIndex - lowerIndex) / 2;
            doMergeSort(lowerIndex, middle);
            doMergeSort(middle + 1, higherIndex);
            mergeParts(lowerIndex, middle, higherIndex);
        }
    }
    private void mergeParts(int lowerIndex, int middle, int higherIndex) {
		for (int i = lowerIndex; i <= higherIndex; i++) {
            tempMergArr[i] = array[i];
        }
        int i = lowerIndex;
        int j = middle + 1;
        int k = lowerIndex;
        while (i <= middle && j <= higherIndex) {
            if (tempMergArr[i] <= tempMergArr[j]) {
                array[k] = tempMergArr[i];
                i++;
            } else {
                array[k] = tempMergArr[j];
                j++;
            }
            k++;
        }
        while (i <= middle) {
            array[k] = tempMergArr[i];
            k++;
            i++;
        }
    }
}