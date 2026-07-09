class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;;

        int size = prices.size();
        int curr_min = 101;

        for (int i = 1; i < size; i++) {
            curr_min = min(curr_min, prices[i-1]);
            int temp = prices[i] - curr_min;

            if (temp > profit) {
                profit = temp;
            }
        }

        return profit;
    }
};
