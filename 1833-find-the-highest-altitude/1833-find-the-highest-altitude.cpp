class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int maxAltitude = 0, currAltitude = 0;

        for (int i = 0; i < gain.size(); i++) {
            currAltitude += gain[i];
            maxAltitude = max(maxAltitude, currAltitude);
        }

        return maxAltitude;
    }
};