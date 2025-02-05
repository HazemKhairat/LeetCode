class Solution {
public:
    bool canPlaceFlowers(vector<int>& f, int n) {
        int count = 0;
        for (int i = 0; i < f.size(); i++) {
            if (f[i] == 0) {
                bool emptyLeftPlot = ((i == 0) || f[i - 1] == 0);
                bool emptyRightPlot = ((i == f.size() - 1) || f[i + 1] == 0);
                if (emptyLeftPlot && emptyRightPlot) {
                    f[i] = 1;
                    count++;
                }
            }
        }

        return count >= n;
    }
};