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
    tree.assign(n + 2, 0);
    for (int k = 0; k < q; k++) {
        int type;
        cin >> type;
        if (type == 1) {
            int l, r;
            long long guests;
            cin >> l >> r >> guests;
            add(l, guests);
            if (r + 1 <= n) {
                add(r + 1, -guests);
            }
        } else {
            int night;
            cin >> night;
            cout << prefix_sum(night) << '\n';
        }
    }
    return 0;
}
