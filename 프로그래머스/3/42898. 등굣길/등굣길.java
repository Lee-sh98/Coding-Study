import java.util.*;
class Solution {
    private static final int MOD = 1_000_000_007;
    public int solution(int m, int n, int[][] puddles) {
        int [][] arr = new int[n+1][m+1];
        int [][] dp = new int[n+1][m+1];
        dp[1][1] = 1;
        
        for(int[] p:puddles){
            arr[p[1]][p[0]] = 1;
        }
        
        for(int i=1; i<=n; i++) {
            for(int j=1; j<=m; j++){
                if(arr[i][j]==1) continue;
                dp[i][j] += (dp[i-1][j]+dp[i][j-1])%MOD;
            }
        }
        
        return (int)dp[n][m];
    }
}