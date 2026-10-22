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
    sort(boxes.begin(), boxes.end(), [](const pair<int, int> &a, const pair<int, int> &b) {
        if (a.first != b.first) {
            return a.first < b.first;
        }
        return a.second > b.second;
    });
    vector<int> tails;
    for (int i = 0; i < n; i++) {
        auto it = lower_bound(tails.begin(), tails.end(), boxes[i].second);
        if (it == tails.end()) {
            tails.push_back(boxes[i].second);
        } else {
            *it = boxes[i].second;
        }
    }
    cout << tails.size() << '\n';
    return 0;
}
