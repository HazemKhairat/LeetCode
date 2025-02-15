class Solution {
public:
    int punishmentNumber(int n) {
        int res = 0;
        for (int i = 1; i <= n; i++) {
            if (partition(0, 0, i, to_string(i * i))) {
                res += (i * i);
            }
        }
        return res;
    }

    bool partition(int index, int currSum, int target, string squareNumStr) {
        if (currSum == target && index == squareNumStr.size()) {
            return true;
        }
        for (int j = index; j < squareNumStr.size(); j++) {
            if (partition(j + 1,
                          currSum +
                              stoi(squareNumStr.substr(index, j - index + 1)),
                          target, squareNumStr)) {
                return true;
            }
        }
        return false;
    }
};