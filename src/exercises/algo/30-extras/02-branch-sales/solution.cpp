#include <bits/stdc++.h>
using namespace std;

int n;
vector<long long> tree;

void add(int i, long long delta)
{
    for (; i <= n; i += i & -i) {
        tree[i] += delta;
    }
}

long long prefix_sum(int i)
{
    long long total = 0;
    for (; i > 0; i -= i & -i) {
        total += tree[i];
    }
    return total;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> n >> q;
    tree.assign(n + 1, 0);
    vector<long long> sales(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> sales[i];
        add(i, sales[i]);
    }
    for (int k = 0; k < q; k++) {
        int type;
        cin >> type;
        if (type == 1) {
            int i;
            long long v;
            cin >> i >> v;
            add(i, v - sales[i]);
            sales[i] = v;
        } else {
            int l, r;
            cin >> l >> r;
            cout << prefix_sum(r) - prefix_sum(l - 1) << '\n';
        }
    }
    return 0;
}
