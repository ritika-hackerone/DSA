class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int l = 0;
        int r = accumulate(nums.begin(), nums.end(), 0);
        for(int i = 0; i<nums.size(); i++){
                r -= nums[i];
                if(r==l) return i;
                l += nums[i];
                
        }
        return -1;
        
    }
};