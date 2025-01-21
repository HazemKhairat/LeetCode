class Solution {
public:
    int bestClosingTime(string c) {
        int n = c.size();
        int res = 0;
        int cost = INT_MAX;
        vector<int> pref(n + 1, 0), suff(n + 2, 0);
        cout << pref[0] << ' ';
        for(int i = 1; i <= n; i++){
            if(c[i - 1] == 'N'){
                pref[i] = pref[i - 1] + 1;
            }
            else{
                pref[i] = pref[i - 1];
            }
            cout << pref[i] << " ";
        }
        cout << endl;
        for(int i = n; i >= 1; i--){
            if(c[i - 1] == 'Y'){
                suff[i] = suff[i + 1] + 1;
            }
            else{
                suff[i] = suff[i + 1];
            }
            
        }
        
        for(int i = 1; i <= n; i++){
            if(cost > pref[i - 1] + suff[i]){
                cost = pref[i - 1] + suff[i];
                res = i - 1;
            }
        }
        if(pref[n] + suff[n + 1] < cost){
            return n;
        }
        for(auto i :  suff){
            cout << i <<  ' ';
        }
        return res;
    }
    
};