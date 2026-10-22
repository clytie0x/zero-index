#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> busy;
    priority_queue<int, vector<int>, greater<int>> idle;
    for (int id = 1; id <= k; id++) {
        idle.push(id);
    }
    long long last_start = 0;
    for (int i = 0; i < n; i++) {
        long long arrive, duration;
        cin >> arrive >> duration;
        long long now = max(arrive, last_start);
        while (!busy.empty() && busy.top().first <= now) {
            idle.push(busy.top().second);
            busy.pop();
        }
        if (idle.empty()) {
            now = busy.top().first;
            while (!busy.empty() && busy.top().first == now) {
                idle.push(busy.top().second);
                busy.pop();
            }
        }
        int machine = idle.top();
        idle.pop();
        busy.push({now + duration, machine});
        last_start = now;
        cout << machine << ' ' << now + duration << '\n';
    }
    return 0;
}
