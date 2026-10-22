#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    set<int> inserted;
    map<int, int> depth;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        int d = 0;
        auto after = inserted.lower_bound(x);
        if (after != inserted.end()) {
            d = max(d, depth[*after] + 1);
        }
        if (after != inserted.begin()) {
            d = max(d, depth[*prev(after)] + 1);
        }
        inserted.insert(x);
        depth[x] = d;
        if (i > 0) {
            cout << ' ';
        }
        cout << d;
    }
    cout << '\n';
    return 0;
}
