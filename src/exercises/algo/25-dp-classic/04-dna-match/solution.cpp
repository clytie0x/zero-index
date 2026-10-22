#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s, t;
    cin >> s >> t;
    int n = s.size(), m = t.size();
    vector<int> above(m + 1, 0), row(m + 1, 0);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (s[i - 1] == t[j - 1]) {
                row[j] = above[j - 1] + 1;
            } else {
                row[j] = max(above[j], row[j - 1]);
            }
        }
        swap(above, row);
    }
    cout << above[m] << '\n';
    return 0;
}
