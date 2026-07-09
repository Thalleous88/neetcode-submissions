class Solution {
public:
    int maxArea(vector<int>& heights) {
        int max = 0;
        int i = 0;
        int j = heights.size()-1;

        while (i < j) {
            int temp = min(heights[i], heights[j]) * (j-i);

            if (temp > max) {
                max = temp;
            }

            if (heights[i] > heights[j]) {
                j--;
            } else {
                i++;
            }
        }

        return max;
    }
};
