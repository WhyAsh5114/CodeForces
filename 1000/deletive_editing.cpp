#include <bits/stdc++.h>
#define endl "\n"

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    while (t--) {
        string s, t;
        cin >> s >> t;
        map<char, int> sa;
        for (char c: s) {
            sa[c] += 1;
        }

        map<char, int> st;
        for (char c : t) {
            st[c] += 1;
        }

        bool num_valid = true;
        for (pair<char, int> p : st) {
            if(p.second > sa[p.first]) {
                num_valid = false;
                cout << "NO" << endl;
                break;
            }
        }

        if (!num_valid)
            continue;
        
        for (pair<char, int> p: sa) {
            int to_drop = p.second - st[p.first];
            for (int i = 0; i < to_drop; i++) {
                int pos = s.find(p.first);
                if (pos != s.npos) {
                    s.erase(s.begin() + pos);
                }
            }
        }

        if (s == t) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
}