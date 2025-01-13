class Solution {
public:
    bool canBeValid(string s, string locked) {
        stack<int> lockedOpen, unlockedFree;

        for (int i = 0; i < s.size(); i++) {
            if (locked[i] == '0') {
                unlockedFree.push(i);
            } else if (s[i] == '(') {
                lockedOpen.push(i);
            } else {
                if (!lockedOpen.empty()) {
                    lockedOpen.pop();
                } else if (!unlockedFree.empty()) {
                    unlockedFree.pop();
                } else {
                    return false;
                }
            }
        }

        while (!lockedOpen.empty() && !unlockedFree.empty() &&
               lockedOpen.top() < unlockedFree.top()) {
            unlockedFree.pop();
            lockedOpen.pop();
        }

        if (!lockedOpen.empty()) {
            return false;
        }

        return unlockedFree.size() % 2 == 0;
    }
};