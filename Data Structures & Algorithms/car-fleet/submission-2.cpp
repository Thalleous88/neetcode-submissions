class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {

        int len = position.size();

        int count = 1;
        
        stack<double> s;
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len-i-1; j++) {
                if (position[j] < position[j+1]) {
                    int temp = position[j];
                    position[j] = position[j+1];
                    position[j+1] = temp;

                    int temp2 = speed[j];
                    speed[j] = speed[j+1];
                    speed[j+1] = temp2;
                }
            }
        }

        for (int i = 0; i < len; i++) {
            if (!s.empty() && (double)((double)(target-position[i])/(double)speed[i]) <= s.top()) {
                continue;
            } 
            s.push((double)(target-position[i])/speed[i]);
        }

        return s.size();

        
    }

   
};
