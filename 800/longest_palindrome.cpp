#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    set<string> all_strings;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        all_strings.insert(s);
    }

    vector<string> start;
    vector<string> end;
    string individual_string = "";
    for (string s : all_strings) {
        string rev = s;
        reverse(rev.begin(), rev.end());
        if (all_strings.find(rev) != all_strings.end() && find(start.begin(), start.end(), s) == start.end() && find(end.begin(), end.end(), s) == end.end() && s != rev) {
            start.push_back(s);
            end.push_back(rev);
        } else if (s == rev) {
            individual_string = s;
        }
    }

    string answer = "";
    for (string s : start) {
        answer.append(s);
    }
    answer.append(individual_string);
    reverse(end.begin(), end.end());
    for (string s : end) {
        answer.append(s);
    }

    cout << answer.length() << endl;
    cout << answer << endl;
}