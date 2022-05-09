#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;

    int answers[t];
    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        vector<int> a;
        for (int j = 0; j < n; j++) {
            int c;
            cin >> c;
            a.push_back(c);
        }

        sort(a.begin(), a.end());
        int max_difference = a[0];
        for (int j = 0; j < n-1; j++) {
            int difference = a[j+1] - a[j];
            if (difference > max_difference) {
                max_difference = difference;
            }
        }
        answers[i] = max_difference;
    }

    for (int answer : answers)
        cout << answer << endl;
}