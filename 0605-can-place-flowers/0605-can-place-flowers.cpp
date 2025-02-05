class Solution {
public:
    bool canPlaceFlowers(vector<int>& f, int n) {
        if (n == 0)
            return true;
        if (f.size() == 1)
            return f[0] == 0;
        int maxi = max(evenLoop(f), oddLoop(f));
        return maxi >= n;
    }

    int evenLoop(vector<int>& f) {
        int n = f.size();
        int count = 0;
        if (f[0] != 1 && f[1] != 1) {
            count++;
        }
        if (f.size() % 2 == 1 && f[n - 1] != 1 && f[n - 2] != 1) {
            count++;
        }

        for (int i = 2; i < n - 2; i += 2) {
            if (f[i - 1] != 1 && f[i + 1] != 1 && f[i] != 1) {
                count++;
            }
        }

        return count;
    }

    int oddLoop(vector<int>& f) {
        int n = f.size();
        int count = 0;
        if (f.size() % 2 == 0 && f[n - 1] != 1 && f[n - 2] != 1) {
            count++;
        }
        for (int i = 1; i < n - 1; i += 2) {
            if (f[i - 1] != 1 && f[i + 1] != 1 && f[i] != 1) {
                count++;
            }
        }

        return count;
    }
};