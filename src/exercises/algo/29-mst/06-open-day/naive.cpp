#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<tuple<int, int, int>> roads(m);
    for (int i = 0; i < m; i++) {
        int a, b, day;
        cin >> a >> b >> day;
        roads[i] = {day, a, b};
    }
    sort(roads.begin(), roads.end());
    vector<vector<int>> adj(n + 1);
    vector<int> first_day(n + 1, -1);
    vector<char> seen(n + 1);
    int i = 0;
    while (i < m) {
        int day = get<0>(roads[i]);
        while (i < m && get<0>(roads[i]) == day) {
            adj[get<1>(roads[i])].push_back(get<2>(roads[i]));
            adj[get<2>(roads[i])].push_back(get<1>(roads[i]));
            i++;
        }
        fill(seen.begin(), seen.end(), 0);
        queue<int> q;
        q.push(1);
        seen[1] = 1;
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            if (v != 1 && first_day[v] == -1) {
                first_day[v] = day;
            }
            for (int to : adj[v]) {
                if (!seen[to]) {
                    seen[to] = 1;
                    q.push(to);
                }
            }
        }
    }
    for (int v = 2; v <= n; v++) {
        cout << first_day[v] << (v == n ? '\n' : ' ');
    }
    return 0;
}
