#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    priority_queue<int, vector<int>, greater<int>> best;
    for (int i = 0; i < n; i++) {
        int score;
        cin >> score;
        best.push(score);
        if ((int)best.size() > k) {
            best.pop();
        }
        if ((int)best.size() < k) {
            cout << -1 << '\n';
        } else {
            cout << best.top() << '\n';
        }
    }
    return 0;
}
