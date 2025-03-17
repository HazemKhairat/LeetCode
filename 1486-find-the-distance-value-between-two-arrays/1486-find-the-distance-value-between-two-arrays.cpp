class Solution {
public:
    int findTheDistanceValue(vector<int>& arr1, vector<int>& arr2, int d) {
        sort(arr2.begin(), arr2.end());
        int res = 0;
        for (int i = 0; i < arr1.size(); i++) {
            int count = 0;
            if (search(arr1[i], arr2, d)) {
                res++;
            }
        }
        return res;
    }

    bool search(int val, vector<int>& arr2, int d) {
        int left = 0, right = arr2.size() - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (abs(val - arr2[mid]) <= d) {
                return false;
            } else if (arr2[mid] < val) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return true;
    }
};