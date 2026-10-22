#include <bits/stdc++.h>
using namespace std;

string s, t;

int lcs(int i, int j)
{
    if (i == (int)s.size() || j == (int)t.size()) {
        return 0;
    }
    if (s[i] == t[j]) {
        return 1 + lcs(i + 1, j + 1);
    }
    return max(lcs(i + 1, j), lcs(i, j + 1));
}

int main()
{
    cin >> s >> t;
    cout << lcs(0, 0) << '\n';
    return 0;
}
