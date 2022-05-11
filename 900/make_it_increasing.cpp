#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;

    vector<int> answers;
    while (t--) {
        int n;
        cin >> n;
        int a[n];
        for (int i = 0; i < n; i++)
            cin >> a[i];
        
        int min_ops = 0;
        for (int i = n-1; i > 0; i--) {
            while (a[i] <= a[i-1] && a[i-1] != 0) {
                a[i-1] /= 2;
                min_ops++;
            }
            
            if (a[i] <= a[i-1]) {
                min_ops = -1;
                break;
            }
        }
        answers.push_back(min_ops);
    }

    for (int answer : answers)
        cout << answer << endl;
}