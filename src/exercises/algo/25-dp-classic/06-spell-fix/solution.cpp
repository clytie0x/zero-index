#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s, t;
    cin >> s >> t;
    int n = s.size(), m = t.size();
    vector<int> above(m + 1), row(m + 1);
    for (int j = 0; j <= m; j++) {
        above[j] = j;
    }
    for (int i = 1; i <= n; i++) {
        row[0] = i;
        for (int j = 1; j <= m; j++) {
            if (s[i - 1] == t[j - 1]) {
                row[j] = above[j - 1];
            } else {
                row[j] = 1 + min({above[j - 1], above[j], row[j - 1]});
            }
        }
        swap(above, row);
    }
    cout << above[m] << '\n';
    return 0;
}
