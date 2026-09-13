class Solution {
public:
    long long countCommas(long long n) {
        long long x = 999,ans=0;
        while(x<=1000000000000000){
            ans += max(0ll,(n-x));
            x *= 1000;
            x += 999;  
        }
        return ans;
    }
};