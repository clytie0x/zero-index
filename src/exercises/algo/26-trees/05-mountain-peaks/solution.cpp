#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> parent(n + 1);
    vector<vector<int>> children(n + 1);
    int root = 0;
    for (int v = 1; v <= n; v++) {
        cin >> parent[v];
        if (parent[v] == 0) {
            root = v;
        } else {
            children[parent[v]].push_back(v);
        }
    }
    vector<int> height(n + 1);
    for (int v = 1; v <= n; v++) {
        cin >> height[v];
    }
    vector<int> best(n + 1, 0);
    int peaks = 0;
    stack<int> waiting;
    waiting.push(root);
    while (!waiting.empty()) {
        int v = waiting.top();
        waiting.pop();
        int before = (v == root) ? 0 : best[parent[v]];
        if (height[v] > before) {
            peaks++;
        }
        best[v] = max(before, height[v]);
        for (int c : children[v]) {
            waiting.push(c);
        }
    }
    cout << peaks << '\n';
    return 0;
}
