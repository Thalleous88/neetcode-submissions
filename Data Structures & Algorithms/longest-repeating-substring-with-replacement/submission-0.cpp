class Solution {
public:
    int characterReplacement(string s, int k) {
        int len = s.length();

        if (len == 1) {
            return 1;
        }

        int arr[26] = {0};
        int left = 0, max_length = 0, max_count = 0;
        
        for (int right = 0; right < len; right++) {
            arr[s[right]-'A']++;
            max_count = max(max_count, arr[s[right]-'A']);

            while ((right-left+1) - max_count > k) {
                arr[s[left]-'A']--;
                left++;
            }

            max_length = max(max_length, right-left+1);
        }

        return max_length;
    }
};
