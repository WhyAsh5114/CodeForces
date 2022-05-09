#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;

        int p[n];
        for (int j = 0; j < n; j++) {
            cin >> p[j];
        }
        string s;
        cin >> s;
        map<int, char> h;
        for (int j = 0; j < n; j++) {
            h[p[j]] = s[j];
        }

        int disliked = 1;
        for (char c: s) {
            if (c == '0')
                disliked++;
        }

        int liked = 1;
        int q[n];
        for (auto iter = h.begin(); iter != h.end(); ++iter){
            if (iter->second == '1') {
                q[iter->first - 1] = disliked;
                disliked++;
            } else {
                q[iter->first - 1] = liked;
                liked++;
            }
        }

        for (int j = 0; j < n; j++) {
            cout << q[p[j] - 1] << " ";
        }
        cout << "\n";
    }
}