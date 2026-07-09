class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        int len = tokens.size();
        for (int i = 0; i < len; i++) {
            if (tokens[i] ==  "+") {
                int a = st.top();
                st.pop();
                int b = st.top();
                st.pop();

                int result = a+b;

                st.push(result);
            } else if (tokens[i] == "-") {
                int b = st.top();
                st.pop();
                int a = st.top();
                st.pop();

                int result = a-b;

                st.push(result);
            } else if (tokens[i] == "*") {
                int a = st.top();
                st.pop();
                int b = st.top();
                st.pop();

                int result = a*b;

                st.push(result);
            } else if (tokens[i] == "/") {
                int b = st.top();
                st.pop();
                int a = st.top();
                st.pop();

                int result = a/b;

                st.push(result);
            } else {
                st.push(stoi(tokens[i]));
            }
        }

        return st.top();
    }
};
