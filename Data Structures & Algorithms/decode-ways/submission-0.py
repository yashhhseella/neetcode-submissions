class Solution:
    def numDecodings(self, s: str) -> int:
        # for this problem I think the dp algo is
        # start by considering just the single didgit case and
        # if the this and this.next case is <= 26 then we consider that and increment to cound

        # no leading 0
        # or we could try bisecting the cases and just adding len of the input to it

        dp = {len(s) : 1}
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            ans = dfs(i + 1) # one step
            if i + 1 < len(s) and (
            s[i] == "1" or s[i] == "2" and
            s[i + 1] in "0123456"): # step permission claim
                ans += dfs(i + 2) # two step
            dp[i] = ans # save current step in cache
            return ans
        
        return dfs(0)


        