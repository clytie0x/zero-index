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
    tree[node] = max(tree[2 * node], tree[2 * node + 1]);
}

int first_fit(int need)
{
    if (tree[1] < need) {
        return 0;
    }
    int node = 1, left = 1, right = n;
    while (left < right) {
        int mid = (left + right) / 2;
        if (tree[2 * node] >= need) {
            node = 2 * node;
            right = mid;
        } else {
            node = 2 * node + 1;
            left = mid + 1;
        }
    }
    return left;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> n >> q;
    tree.assign(4 * n, 0);
    vector<int> space(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> space[i];
        update(1, 1, n, i, space[i]);
    }
    for (int j = 0; j < q; j++) {
        int box;
        cin >> box;
        int shelf = first_fit(box);
        if (shelf > 0) {
            space[shelf] -= box;
            update(1, 1, n, shelf, space[shelf]);
        }
        cout << shelf << '\n';
    }
    return 0;
}
