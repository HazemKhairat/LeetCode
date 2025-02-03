class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        sort(letters.begin(), letters.end());
        return binary_search(letters, target);
    }

    char binary_search(vector<char>& letters, char target) {
        int i = 0, j = letters.size() - 1;
        while (i < j) {
            int mid = (i + j) / 2;
            if (letters[mid] <= target) {
                i = mid + 1;
            } else {
                j = mid;
            }
        }
        return j == letters.size() - 1 && letters[j] <= target ? letters[0] : letters[j];
    }
};