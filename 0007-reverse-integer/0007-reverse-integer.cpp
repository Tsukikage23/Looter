class Solution {
public:
    int reverse(int x) {
                long long int rem = 0;
        while(x!=0){
            rem = rem * 10 + x%10;
            x /= 10;
        }
        if(rem <= 2147483647 && rem >= -2147483648){
            return rem;
        }
        else {
            return 0;
        }
    }
};