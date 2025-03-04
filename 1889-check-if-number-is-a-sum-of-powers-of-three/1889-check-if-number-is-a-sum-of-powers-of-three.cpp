class Solution {
public:
    bool checkPowersOfThree(int n) {
        return solve(n, 0, 0);
    }

    bool solve(int& n, int index, int sum){
        // cout << sum << endl;
        if(sum > n){
            return false;
        }
        if(sum == n){
            return true;
        }
        for(int i = index; i <= 16; i++){
            if(solve(n, i + 1, sum + power(i))){
                return true;
            }
        }
        return false;
    }

    int power(int i){
        int pow = 1;
        for(int j = 0; j < i; j++){
            pow *= 3;
        }
        return pow;
    }
};