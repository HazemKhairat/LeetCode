class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        // convert the nums to circle
        // map for each nums[query[i]] to indices of nums == nums[query[i][]
        // for each query find qeries[i] - index , such that is minimum
        // continue if the same
        int n = nums.size();
        vector<int> res;
        unordered_map<int, vector<int>> mp;

        for (int i = 0; i < n; i++) {
            mp[nums[i]].push_back(i);
        }

        for (int query : queries) {
            int value = nums[query];
            vector<int>& arr = mp[value];
            int m = arr.size();
            if (arr.size() == 1) {
                res.push_back(-1);
                continue;
            }
            int index = search(arr, query);

            if (index == m - 1) {
                res.push_back(
                    min(arr[index] - arr[index - 1], n - arr[index] + arr[0]));
            } else if (index == 0) {
                res.push_back(min(arr[index + 1] - arr[index],
                                  n - arr[m - 1] + arr[index]));
            } else {
                res.push_back(min(arr[index] - arr[index - 1],
                                  arr[index + 1] - arr[index]));
            }
        }

        return res;
    }

    int search(vector<int>& v, int q) {
        int i = 0, j = v.size() - 1;
        while (i <= j) {
            int mid = (i + j) / 2;
            if (v[mid] < q) {
                i = mid + 1;
            } else if (v[mid] > q) {
                j = mid - 1;
            } else {
                return mid;
            }
        }
        return i;
    }
};