#include <bits/stdc++.h>
using namespace std;

int n;
vector<long long> change_tree, weighted_tree;

void add(vector<long long> &tree, int i, long long delta)
{
    for (; i <= n; i += i & -i) {
        tree[i] += delta;
    }
}

long long prefix_sum(const vector<long long> &tree, int i)
{
    long long total = 0;
    for (; i > 0; i -= i & -i) {
        total += tree[i];
    }
    return total;
}

void add_change(int night, long long delta)
{
    if (night > n) {
        return;
    }
    add(change_tree, night, delta);
    add(weighted_tree, night, delta * night);
}

long long guest_nights_up_to(int x)
{
    return (x + 1) * prefix_sum(change_tree, x) - prefix_sum(weighted_tree, x);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> n >> q;
    change_tree.assign(n + 1, 0);
    weighted_tree.assign(n + 1, 0);
    for (int k = 0; k < q; k++) {
        int type, l, r;
        cin >> type >> l >> r;
        if (type == 1) {
            long long guests;
            cin >> guests;
            add_change(l, guests);
            add_change(r + 1, -guests);
        } else {
            cout << guest_nights_up_to(r) - guest_nights_up_to(l - 1) << '\n';
        }
    }
    return 0;
}
