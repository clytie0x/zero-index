#include <bits/stdc++.h>
using namespace std;

int inside[1000001];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> song(n);
    for (int i = 0; i < n; i++) {
        cin >> song[i];
    }
    int best = 0, best_start = 0;
    int l = 0;
    for (int r = 0; r < n; r++) {
        inside[song[r]]++;
        while (inside[song[r]] > 1) {
            inside[song[l]]--;
            l++;
        }
        if (r - l + 1 > best) {
            best = r - l + 1;
            best_start = l;
        }
    }
    cout << best << ' ' << best_start + 1 << '\n';
    return 0;
}
