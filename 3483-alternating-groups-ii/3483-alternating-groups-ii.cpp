class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors, int k) {
        int n = colors.size();
        int res = 0;
        vector<int> doubleColors(colors.begin(), colors.end());
        for (auto co : colors) {
            doubleColors.push_back(co);
        }

        int i = 0, j = i + 1;
        while ((j < n + n) && (i < n)) {
            // cout << i << " " << j << " " << res << endl;
            if (doubleColors[j] != doubleColors[j - 1]) {
                if (j - i + 1 == k) {
                    res++;
                    i++;
                }
            } else {
                i = j;
            }
            j++;
        }

        return res;
    }
};