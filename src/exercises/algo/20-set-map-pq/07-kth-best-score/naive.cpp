#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    vector<int> scores;
    for (int i = 0; i < n; i++) {
        int score;
        cin >> score;
        scores.push_back(score);
        int j = (int)scores.size() - 1;
        while (j > 0 && scores[j - 1] < score) {
            scores[j] = scores[j - 1];
            j--;
        }
        scores[j] = score;
        if ((int)scores.size() < k) {
            cout << -1 << '\n';
        } else {
            cout << scores[k - 1] << '\n';
        }
    }
    return 0;
}
