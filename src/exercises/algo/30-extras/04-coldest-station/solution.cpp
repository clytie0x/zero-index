#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> tree;

void update(int node, int left, int right, int pos, int value)
{
    if (left == right) {
        tree[node] = value;
        return;
    }
    int mid = (left + right) / 2;
    if (pos <= mid) {
        update(2 * node, left, mid, pos, value);
    } else {
        update(2 * node + 1, mid + 1, right, pos, value);
    }
    tree[node] = min(tree[2 * node], tree[2 * node + 1]);
}

int query(int node, int left, int right, int from, int to)
{
    if (to < left || right < from) {
        return INT_MAX;
    }
    if (from <= left && right <= to) {
        return tree[node];
    }
    int mid = (left + right) / 2;
    return min(query(2 * node, left, mid, from, to), query(2 * node + 1, mid + 1, right, from, to));
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> n >> q;
    tree.assign(4 * n, INT_MAX);
    for (int i = 1; i <= n; i++) {
        int t;
        cin >> t;
        update(1, 1, n, i, t);
    }
    for (int k = 0; k < q; k++) {
        int type, a, b;
        cin >> type >> a >> b;
        if (type == 1) {
            update(1, 1, n, a, b);
        } else {
            cout << query(1, 1, n, a, b) << '\n';
        }
    }
    return 0;
}
