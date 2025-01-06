class Solution {
public:
    vector<int> minOperations(string boxes) {
        int n = boxes.size();
        vector<int> ans(n);
        int leftBalls = 0, movesToLeft = 0;
        int rightBalls = 0, movesToRight = 0;

        for(int i = 0; i < n; i++){
            ans[i] += movesToLeft;
            leftBalls += boxes[i] - '0';
            movesToLeft += leftBalls;

            int j = n - 1 - i;
            ans[j] += movesToRight;
            rightBalls += boxes[j] - '0';
            movesToRight += rightBalls;
        }
        
        return ans;
    }
};