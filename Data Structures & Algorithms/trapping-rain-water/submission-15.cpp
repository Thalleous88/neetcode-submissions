class Solution {
public:
    int trap(vector<int>& height) {
        int i = 0;
        int j = 1;

        int len = height.size()-1;

        if (height.size() < 3) {
            return 0;
        }

        int maxw = 0;
        while (i < len) {
            while (height[i] == 0 && i < len) {
                i++;
                j = i + 1;
            }

            while (j < len && height[j] < height[i]) {
                j++;
            }
        

            if (j == len) {
                int maxIndex = i + 1;
                for (int k = i + 1; k <= len; k++) {
                    if (height[k] > height[maxIndex])
                        maxIndex = k;
                }
                j = maxIndex;
            }
                
            for (int x = i+1; x < j; x++) {
                maxw += min(height[i], height[j]) - height[x];
            }

            

            i = j;
            j = i+1;
        }

        return maxw;
    }
};
