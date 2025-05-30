class Solution {
public:
    long long countOfSubstrings(string word, int k) {
        int n = word.size();
        map<char, int> vowels;
        int consonantCount = 0;
        long long res = 0;

        vector<int> nextConsonant(n);
        int lastConsonant = n;
        for (int i = n - 1; i >= 0; i--) {
            nextConsonant[i] = lastConsonant;
            if (!isVowel(word[i])) {
                lastConsonant = i;
            }
        }

        int left = 0, right = 0;
        while (right < n) {
            if (isVowel(word[right])) {
                vowels[word[right]]++;
            } else {
                consonantCount++;
            }

            while (left <= right && consonantCount > k) {
                if (isVowel(word[left])) {
                    if (--vowels[word[left]] == 0) {
                        vowels.erase(word[left]);
                    }
                } else {
                    consonantCount--;
                }
                left++;
            }

            while (left < right && vowels.size() == 5 && consonantCount == k) {
                res += (nextConsonant[right] - right);
                if (isVowel(word[left])) {
                    if (--vowels[word[left]] == 0) {
                        vowels.erase(word[left]);
                    }
                } else {
                    consonantCount--;
                }
                left++;
            }
            right++;
        }
        return res;
    }

    bool isVowel(char ch) {
        return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
    }
};