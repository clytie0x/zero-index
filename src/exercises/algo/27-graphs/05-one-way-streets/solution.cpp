#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200001;
vector<int> out_roads[MAXN];
vector<int> in_roads[MAXN];

// รับอาเรย์ของ vector แบบเดียวกับส่งอาเรย์เข้าฟังก์ชันในหน้า 8.3 ฟังก์ชันใช้ตัวจริง ไม่ได้คัดลอก
vector<bool> reachable(int n, vector<int> roads[])
{
    vector<bool> seen(n + 1, false);
    queue<int> waiting;
    seen[1] = true;
    waiting.push(1);
    while (!waiting.empty()) {
        int v = waiting.front();
        waiting.pop();
        for (int next : roads[v]) {
            if (!seen[next]) {
                seen[next] = true;
                waiting.push(next);
            }
        }
    }
    return seen;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int from, to;
        cin >> from >> to;
        out_roads[from].push_back(to);
        in_roads[to].push_back(from);
    }
    vector<bool> go = reachable(n, out_roads);
    vector<bool> back = reachable(n, in_roads);
    int go_count = 0, back_count = 0, both = 0;
    for (int v = 2; v <= n; v++) {
        go_count += go[v]; // true บวกเป็น 1 false บวกเป็น 0
        back_count += back[v];
        both += go[v] && back[v];
    }
    cout << go_count << ' ' << back_count << ' ' << both << '\n';
    return 0;
}
