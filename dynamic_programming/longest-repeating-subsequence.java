import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);

    int t = sc.nextInt();
    while (t > 0) {
      t--;
      // read the string length, and the string
      int n = sc.nextInt();
      sc.nextLine();
      String s = sc.nextLine();
      // print the length of the longest repeating subsequence in s
      System.out.println(LRS(s, n));
    }
	}

  public static int LRS(String s, int n) {
    int[][] memo = new int[n+1][n+1];
    for (int i = 0; i <= n; i++) {
      for (int j = 0; j <= n; j++) {
        memo[i][j] = 0;
      }
    }

    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        if (s.charAt(i-1) == s.charAt(j-1) && i != j) {
          memo[i][j] = 1 + memo[i-1][j-1];
        } else {
          memo[i][j] = Math.max(memo[i][j-1], memo[i-1][j]);
        }
      }
    }

    return memo[n][n];
  }
}
