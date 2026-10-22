#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<int> room(n + 1), members(n + 1, 1);
    for (int i = 1; i <= n; i++) {
        room[i] = i;
    }
    for (int k = 0; k < q; k++) {
        int type, a;
        cin >> type >> a;
        if (type == 1) {
            int b;
            cin >> b;
            int to = room[a];
            int from = room[b];
            if (to == from) {
                continue;
            }
            for (int u = 1; u <= n; u++) {
                if (room[u] == from) {
                    room[u] = to;
                }
            }
            members[to] += members[from];
        } else {
            cout << room[a] << ' ' << members[room[a]] << '\n';
        }
    }
    return 0;
}
