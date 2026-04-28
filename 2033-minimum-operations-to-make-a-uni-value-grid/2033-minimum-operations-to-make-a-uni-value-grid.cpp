class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        // we can not make two integers a and b equal
        // if they have different remainders dividing by x.
        // will sorting be helpfule ?
        // 2 4 6 8  -> equation = (num - mid) / x
        // more ex : 1 2 3 5 -> ok it works well

        vector<int> sorted;
        int rem = grid[0][0] % x;

        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] % x != rem) {
                    return -1;
                } else {
                    sorted.push_back(grid[i][j]);
                }
            }
        }

        sort(sorted.begin(), sorted.end());
        int mid = (sorted.size() / 2);
        int res = 0;

        for (int i = mid + 1; i < sorted.size(); i++) {
            res += (sorted[i] - sorted[mid]) / x;
        }
        for (int i = mid - 1; i < sorted.size(); i--) {
            res += (sorted[mid] - sorted[i]) / x;
        }

        return res;
    }
};