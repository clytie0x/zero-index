#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<int> group(n + 1), group_size(n + 1, 1);
    for (int i = 1; i <= n; i++) {
        group[i] = i;
    }
    long long pairs = 0;
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        int from = group[b];
        int to = group[a];
        if (from != to) {
            pairs += (long long)group_size[to] * group_size[from];
            for (int s = 1; s <= n; s++) {
                if (group[s] == from) {
                    group[s] = to;
                }
            }
            group_size[to] += group_size[from];
        }
        cout << pairs << '\n';
    }
    return 0;
}
