import java.util.*;
class Solution {
    private static final int MOD = 1_000_000_007;
    public int solution(int m, int n, int[][] puddles) {
        int [][] arr = new int[n][m];
        int [][] dp = new int[n][m];
        dp[0][0] = 1;
        
        for(int[] p:puddles){
            arr[p[1]-1][p[0]-1] = 1;
        }
        
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++){
                if(arr[i][j]==1) {continue;}
                if(i==0&&j==0) {continue;}
                
                if(i==0){
                    dp[i][j] += dp[i][j-1];
                }else if(j==0){
                    dp[i][j] += dp[i-1][j];
                }
                else {
                    dp[i][j] += dp[i-1][j] + dp[i][j-1];
                }
                dp[i][j] %= MOD;
            }
        }
        
        return (int)dp[n-1][m-1];
    }
}