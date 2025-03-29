class Solution {
public:
    int reverseDegree(string s) {
        int sum = 0;
        for(int i = 1; i <= s.size(); i++){
            sum += (26 - (s[i - 1] - 97)) * i;
        }
        return sum;
    }
};