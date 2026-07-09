class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> st;

        int len = temperatures.size();

        vector<int> res;

        int i = 0;
        
        while (i < len) {
            
            int j = i;
            int count = 0;

            st.push(temperatures[i]);
            while (temperatures[j] <= st.top()) {
                j++;
                count++;
            }

            if (j >= len-1 && temperatures[i] >= temperatures[len-1]) {
                res.push_back(0);
            } else {
                res.push_back(count);
            }

            i++;
        }

        return res;
    }
};
