#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> level(n);
    for (int i = 0; i < n; i++) {
        cin >> level[i];
    }
    for (int i = 0; i < n; i++) {
        int j = i;
        while (j > 0 && level[j - 1] <= level[i]) {
            j--;
        }
        cout << i - j + 1 << (i + 1 < n ? ' ' : '\n');
    }
    return 0;
}
