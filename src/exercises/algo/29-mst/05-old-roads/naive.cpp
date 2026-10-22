#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> parent, group_size;
vector<pair<int, int>> old_roads;
vector<tuple<int, int, int>> roads;

int find_root(int x)
{
    if (parent[x] == x) {
        return x;
    }
    parent[x] = find_root(parent[x]);
    return parent[x];
}

bool unite(int a, int b)
{
    int root_a = find_root(a);
    int root_b = find_root(b);
    if (root_a == root_b) {
        return false;
    }
    if (group_size[root_a] < group_size[root_b]) {
        swap(root_a, root_b);
    }
    parent[root_b] = root_a;
    group_size[root_a] += group_size[root_b];
    return true;
}

// ให้บริษัทจ่ายแนวที่ sponsored แล้วทำ Kruskal ใหม่ทั้งหมด sponsored เป็น -1 คือไม่มีแนวไหนฟรี
long long cost_with(int sponsored)
{
    parent.resize(n + 1);
    group_size.assign(n + 1, 1);
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }
    int groups = n;
    for (auto [a, b] : old_roads) {
        if (unite(a, b)) {
            groups--;
        }
    }
    if (sponsored != -1 && unite(get<1>(roads[sponsored]), get<2>(roads[sponsored]))) {
        groups--;
    }
    long long total = 0;
    for (int i = 0; i < (int)roads.size(); i++) {
        auto [cost, a, b] = roads[i];
        if (i != sponsored && unite(a, b)) {
            groups--;
            total += cost;
        }
    }
    return groups == 1 ? total : -1;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int k, m;
    cin >> n >> k >> m;
    old_roads.resize(k);
    for (int i = 0; i < k; i++) {
        cin >> old_roads[i].first >> old_roads[i].second;
    }
    roads.resize(m);
    for (int i = 0; i < m; i++) {
        int a, b, cost;
        cin >> a >> b >> cost;
        roads[i] = {cost, a, b};
    }
    sort(roads.begin(), roads.end());
    long long best = cost_with(-1);
    if (best > 0) {
        for (int i = 0; i < m; i++) {
            best = min(best, cost_with(i));
        }
    }
    cout << best << '\n';
    return 0;
}
