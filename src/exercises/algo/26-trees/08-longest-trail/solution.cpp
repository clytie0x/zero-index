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
    vector<long long> length(n + 1);
    for (int v = 1; v <= n; v++) {
        cin >> length[v];
    }
    vector<int> order;
    stack<int> waiting;
    waiting.push(root);
    while (!waiting.empty()) {
        int v = waiting.top();
        waiting.pop();
        order.push_back(v);
        for (int c : children[v]) {
            waiting.push(c);
        }
    }
    vector<long long> longest(n + 1, 0), second(n + 1, 0);
    long long answer = 0;
    for (int i = n - 1; i >= 0; i--) {
        int v = order[i];
        answer = max(answer, longest[v] + second[v]);
        int p = parent[v];
        if (p == 0) {
            continue;
        }
        long long down = longest[v] + length[v];
        if (down > longest[p]) {
            second[p] = longest[p];
            longest[p] = down;
        } else if (down > second[p]) {
            second[p] = down;
        }
    }
    cout << answer << '\n';
    return 0;
}
