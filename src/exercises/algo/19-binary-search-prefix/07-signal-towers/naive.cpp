#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, towers;
    cin >> n >> towers;
    vector<int> spots(n);
    for (int i = 0; i < n; i++) {
        cin >> spots[i];
    }
    sort(spots.begin(), spots.end());
    int best = 0;
    for (int a = 0; a < n; a++) {
        for (int b = a + 1; b < n; b++) {
            int gap = spots[b] - spots[a];
            if (gap <= best) {
                continue;
            }
            int placed = 1;
            int last = spots[0];
            for (int i = 1; i < n; i++) {
                if (spots[i] - last >= gap) {
                    placed++;
                    last = spots[i];
                }
            }
            if (placed >= towers) {
                best = gap;
            }
        }
    }
    cout << best << '\n';
    return 0;
}
