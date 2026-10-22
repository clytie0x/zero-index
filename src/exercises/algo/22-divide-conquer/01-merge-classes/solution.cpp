#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<int> room_a(n), room_b(m);
    for (int i = 0; i < n; i++) {
        cin >> room_a[i];
    }
    for (int j = 0; j < m; j++) {
        cin >> room_b[j];
    }
    vector<int> merged;
    merged.reserve(n + m);
    int i = 0, j = 0;
    while (i < n && j < m) {
        if (room_a[i] <= room_b[j]) {
            merged.push_back(room_a[i]);
            i++;
        } else {
            merged.push_back(room_b[j]);
            j++;
        }
    }
    while (i < n) {
        merged.push_back(room_a[i]);
        i++;
    }
    while (j < m) {
        merged.push_back(room_b[j]);
        j++;
    }
    for (int k = 0; k < n + m; k++) {
        cout << merged[k] << (k == n + m - 1 ? '\n' : ' ');
    }
    return 0;
}
