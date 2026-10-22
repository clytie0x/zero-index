#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, s;
    cin >> n >> m >> s;
    vector<int> a(m), b(m);
    for (int i = 0; i < m; i++) {
        cin >> a[i] >> b[i];
    }
    vector<int> heard_on(n + 1, -1);
    heard_on[s] = 0;
    int last_day = 0;
    for (int day = 1; ; day++) {
        bool changed = false;
        for (int i = 0; i < m; i++) {
            if (heard_on[a[i]] != -1 && heard_on[a[i]] < day && heard_on[b[i]] == -1) {
                heard_on[b[i]] = day;
                changed = true;
            }
            if (heard_on[b[i]] != -1 && heard_on[b[i]] < day && heard_on[a[i]] == -1) {
                heard_on[a[i]] = day;
                changed = true;
            }
        }
        if (!changed) {
            break;
        }
        last_day = day;
    }
    int count = 0;
    for (int v = 1; v <= n; v++) {
        if (heard_on[v] != -1) {
            count++;
        }
    }
    cout << count << ' ' << last_day << '\n';
    return 0;
}
