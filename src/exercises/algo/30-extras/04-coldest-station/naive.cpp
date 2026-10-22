#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<int> temperature(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> temperature[i];
    }
    for (int k = 0; k < q; k++) {
        int type, a, b;
        cin >> type >> a >> b;
        if (type == 1) {
            temperature[a] = b;
        } else {
            int station = a;
            for (int i = a + 1; i <= b; i++) {
                if (temperature[i] < temperature[station]) {
                    station = i;
                }
            }
            cout << temperature[station] << ' ' << station << '\n';
        }
    }
    return 0;
}
