#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<vector<int>> children(n + 1);
    int root = 0;
    for (int v = 1; v <= n; v++) {
        int p;
        cin >> p;
        if (p == 0) {
            root = v;
        } else {
            children[p].push_back(v);
        }
    }
    vector<int> depth(n + 1, 0), count_at;
    queue<int> waiting;
    waiting.push(root);
    while (!waiting.empty()) {
        int v = waiting.front();
        waiting.pop();
        if (depth[v] == (int)count_at.size()) {
            count_at.push_back(0);
        }
        count_at[depth[v]]++;
        for (int c : children[v]) {
            depth[c] = depth[v] + 1;
            waiting.push(c);
        }
    }
    for (int k = 0; k < (int)count_at.size(); k++) {
        if (k > 0) {
            cout << ' ';
        }
        cout << count_at[k];
    }
    cout << '\n';
    return 0;
}
