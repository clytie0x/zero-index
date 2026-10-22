#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<pair<int, int>> boxes(n);
    for (int i = 0; i < n; i++) {
        cin >> boxes[i].first >> boxes[i].second;
    }
    sort(boxes.begin(), boxes.end());
    vector<int> length(n, 1);
    int best = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (boxes[j].first < boxes[i].first && boxes[j].second < boxes[i].second) {
                length[i] = max(length[i], length[j] + 1);
            }
        }
        best = max(best, length[i]);
    }
    cout << best << '\n';
    return 0;
}
