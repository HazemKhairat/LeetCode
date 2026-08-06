class Solution {
public:
    int smallestNumber(int n, int t) {
        for(int i = n; ; i++){
            int tmp = i;
            int product = 1;
            while(tmp){
                product *= (tmp % 10);
                tmp /= 10;
            }
            if(product % t == 0){
                return i;
            }
        }
        return 0;
    }
};