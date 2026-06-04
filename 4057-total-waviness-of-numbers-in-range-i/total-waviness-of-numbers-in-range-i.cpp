class Solution {
public:
    struct Node {
        long long cnt;
        long long wav;
    };

    string s;
    Node dp[20][11][11][2][2];
    bool vis[20][11][11][2][2];

    Node dfs(int pos, int prev2, int prev1, bool tight, bool started) {
        if (pos == s.size()) {
            return {1, 0};
        }

        if (!tight && vis[pos][prev2 + 1][prev1 + 1][started][0]) {
            return dp[pos][prev2 + 1][prev1 + 1][started][0];
        }

        int limit = tight ? (s[pos] - '0') : 9;

        long long totalCnt = 0;
        long long totalWav = 0;

        for (int d = 0; d <= limit; d++) {
            bool ntight = tight && (d == limit);

            if (!started && d == 0) {
                Node nxt = dfs(pos + 1, -1, -1, ntight, false);
                totalCnt += nxt.cnt;
                totalWav += nxt.wav;
            }
            else if (!started) {
                Node nxt = dfs(pos + 1, -1, d, ntight, true);
                totalCnt += nxt.cnt;
                totalWav += nxt.wav;
            }
            else {
                int add = 0;

                if (prev2 != -1) {
                    bool peak =
                        (prev1 > prev2 && prev1 > d);

                    bool valley =
                        (prev1 < prev2 && prev1 < d);

                    if (peak || valley)
                        add = 1;
                }

                Node nxt = dfs(pos + 1, prev1, d, ntight, true);

                totalCnt += nxt.cnt;
                totalWav += nxt.wav + 1LL * add * nxt.cnt;
            }
        }

        Node res = {totalCnt, totalWav};

        if (!tight) {
            vis[pos][prev2 + 1][prev1 + 1][started][0] = true;
            dp[pos][prev2 + 1][prev1 + 1][started][0] = res;
        }

        return res;
    }

    long long solve(long long n) {
        if (n < 0) return 0;

        s = to_string(n);
        memset(vis, 0, sizeof(vis));

        return dfs(0, -1, -1, true, false).wav;
    }

    long long totalWaviness(long long num1, long long num2) {
        return solve(num2) - solve(num1 - 1);
    }
};