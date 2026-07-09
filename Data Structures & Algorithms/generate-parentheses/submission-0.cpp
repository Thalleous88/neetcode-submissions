class Solution {
public:
    void backtrack(int open, int close, int n, vector<string>& res, string& st) {
        if (open == close && open == n) {
            res.push_back(st);
        }

        if (open < n) {
            st += '(';
            backtrack(open+1, close, n, res, st);

            st.pop_back();
        }

        if (close < open) {
            st += ')';
            backtrack(open, close+1, n, res, st);
            
            st.pop_back();
        }
    }

    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string st;

        backtrack(0, 0, n, res, st);
        return res;
    }
};
