class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        map<int, int> mp;
        for(auto item : arr){
            mp[item] = 1;
        }
        int i = 1;
        auto it = mp.begin();
        for(int i = 0; i < mp.size(); i++){
            it->second = i + 1;
            it++;
        }
        for(int i = 0; i < arr.size(); i++){
            arr[i] = mp[arr[i]];
        }
        return arr;
    }
};