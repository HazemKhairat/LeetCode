class Solution {
public:
    bool canConstruct(string s, int k) {
        if(s.size() < k) return false;

        int oddCount = 0;
        for(auto ch : s){
            oddCount ^= (1 << (ch - 'a'));
        }
        int setBit = 0;
        while(oddCount){
            setBit += (1 & oddCount);
            oddCount >>= 1;
        }

        return setBit <= k;
    }
};