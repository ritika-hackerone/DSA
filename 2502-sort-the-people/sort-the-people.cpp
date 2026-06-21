class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        map<int,string, greater<int>> map;
        for (int i = 0; i<names.size(); i++){
            map[heights[i]] = names[i];
        }
        vector<string> ans ;
        for (auto &i: map){
            ans.push_back(i.second);
        }
        return ans;
    }
        
};