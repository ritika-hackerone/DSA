class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int s = nums.size();
        vector<int>ans(s);
        int n = 1, p = 0;
        for(int i:nums){
                if(i<0){
                    ans[n] = i;
                    n+=2;
                }
                else{
                    ans[p]= i;
                    p+=2;
                }
        }
        return ans;
        
    }
};