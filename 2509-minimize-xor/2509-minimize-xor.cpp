class Solution {
public:
    int minimizeXor(int num1, int num2) {
        int setBits = 0;
        while (num2) {
            if (num2 & 1) {
                setBits++;
            }
            num2 >>= 1;
        }
        cout << setBits << endl;
        vector<int> arr1(32, 0), arr2(32, 0);

        for (int i = 0; i < 32; i++) {
            arr1[i] = (1 & num1);
            cout << arr1[i] << " ";
            num1 >>= 1;
        }
        cout << endl;

        for (int i = 31; i >= 0; i--) {
            if (arr1[i] == 1 && setBits) {
                arr2[i] = 1;
                setBits--;
            }
            cout << arr2[i] << " ";
        }
        cout << endl;
        for (int i = 0; i < 32; i++) {
            if (setBits == 0)
                break;
            if (arr2[i] == 0) {
                arr2[i] = 1;
                setBits--;
            }
            cout << arr2[i] << " ";
        }

        int res = 0;
        for (int i = 31; i >= 0; i--) {
            res |= arr2[i];
            res <<= 1;
        }
        res >>= 1;
        return res;
    }
};