#include <bits/stdc++.h>
using namespace std;

bool playing[1000001];

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
    for (int l = 0; l < n; l++) {
        int r = l;
        while (r < n && !playing[song[r]]) {
            playing[song[r]] = true;
            r++;
        }
        if (r - l > best) {
            best = r - l;
            best_start = l;
        }
        for (int i = l; i < r; i++) {
            playing[song[i]] = false;
        }
    }
    cout << best << ' ' << best_start + 1 << '\n';
    return 0;
}
