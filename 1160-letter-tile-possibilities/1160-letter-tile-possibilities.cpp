class Solution {
public:
    int numTilePossibilities(string tiles) {
        map<char, int> freq;
        for (auto ch : tiles) {
            freq[ch]++;
        }
        return backtrack(freq);
    }

    int backtrack(map<char, int>& freq) {
        int count = 0;
        for (auto item : freq) {
            char ch = item.first;
            int num = item.second;
            if (num == 0) {
                continue;
            }

            count++;
            freq[ch]--;
            count += backtrack(freq);
            freq[ch]++;
        }

        return count;
    }
};