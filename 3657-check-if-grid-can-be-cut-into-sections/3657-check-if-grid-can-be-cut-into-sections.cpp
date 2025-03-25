class Solution {
public:
    bool checkValidCuts(int n, vector<vector<int>>& rectangles) {
        vector<vector<int>> horizontal, vertical;

        for (auto rectangle : rectangles) {
            horizontal.push_back({rectangle[1], rectangle[3]});
            vertical.push_back({rectangle[0], rectangle[2]});
        }
        sort(horizontal.begin(), horizontal.end());
        sort(vertical.begin(), vertical.end());

        int towH = 0, towV = 0, maxEndH = horizontal[0][1], maxEndV = vertical[0][1];
        for (int i = 1; i < horizontal.size(); i++) {
            if (horizontal[i][0] >= maxEndH) {
                towH++;
                if (towH == 2) {
                    return true;
                }
            }
            // cout << vertical[i - 1][1]  << " , " << vertical[i][0]  << endl;
            // cout << horizontal[i - 1][1]  << " , " << horizontal[i][0]  << endl;
            if (vertical[i][0] >= maxEndV) {
                towV++;
                if (towV == 2) {
                    return true;
                }
            }
            maxEndH = max(maxEndH, horizontal[i][1]);
            maxEndV = max(maxEndV, vertical[i][1]);
        }

        return false;
    }
};