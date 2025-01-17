class Solution {
public:
    bool doesValidArrayExist(vector<int>& derived) {
        int n = derived.size();

        vector<int> original = {0};
        for(int i = 0; i < n; i++){
            original.push_back(derived[i] ^ original[i]);
        }
        int caseZero = (original[0] == original.back());

        original = {1};
        for(int i = 0; i < n; i++){
            original.push_back(derived[i] ^ original[i]);
        }
        int caseOne = (original[0] == original.back());

        return (caseZero || caseOne);

    }
};