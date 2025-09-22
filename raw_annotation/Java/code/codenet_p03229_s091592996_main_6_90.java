import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		long[]A = new long[N];
		for(int i = 0; i < N; i++) {
			A[i] = sc.nextLong();
		}
		sc.close();
		Arrays.sort(A);
		long[]B = new long[N];
		if(N == 3) {
			B[0] = A[2];
			B[1] = A[0];
			B[2] = A[1];
			System.out.println(sum(B));
			System.exit(0);
		}
		int l = N / 2;
		if(N % 2 == 1) {
			Deque<Long> st1 = new ArrayDeque<Long>();
			Deque<Long> st2 = new ArrayDeque<Long>();
			for(int i = 1; i <= l; i++) {
				st1.addLast(A[i]);
			}
			for(int i = l + 1; i < N; i++) {
				st2.addFirst(A[i]);
			}
			int t = 1;
			B[l] = A[0];
			for(int i = 0; i < N; i++) {
				if(i == l) {
					t = -1;
					continue;
				}
				if(t == 1) {
					B[i] = st1.pollLast();
				}else {
					B[i] = st2.pollFirst();
				}
				t *= -1;
			}
			long s = sum(B);
			System.out.println(sum(B));
			for(int i = 1; i <= l; i++) {
				st1.addLast(A[i]);
			}
			for(int i = l + 1; i < N; i++) {
				st2.addFirst(A[i]);
			}
			t = -1;
			B[l] = A[0];
			for(int i = 0; i < N; i++) {
				if(i == l) {
					t = -1;
					continue;
				}
				if(t == 1) {
					B[i] = st1.pollLast();
				}else {
					B[i] = st2.pollFirst();
				}
				t *= -1;
			}
			s = Math.max(s, sum(B));
		}else {
			Deque<Long> st1 = new ArrayDeque<Long>();
			Deque<Long> st2 = new ArrayDeque<Long>();
			for(int i = 0; i < l; i++) {
				st1.addLast(A[i]);
			}
			for(int i = l; i < N; i++) {
				st2.addFirst(A[i]);
			}
			int t = 1;
			for(int i = 0; i < N; i++) {
				if(t == 1) {
					B[i] = st1.pollLast();
				}else {
					B[i] = st2.pollFirst();
				}
				t *= -1;
			}
			System.out.println(sum(B));
		}
	}
	static void disp(long[]a) {
		for(long i : a) {
			System.out.print(i + " ");
		}
		System.out.println();
	}
	static long sum(long[]a) {
		long t = 0;
		for(int i = 1; i < a.length; i++) {
			t += Math.abs(a[i] - a[i - 1]);
		}
		return t;
	}
}