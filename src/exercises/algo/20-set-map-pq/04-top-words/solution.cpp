#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    map<string, int> count;
    for (int i = 0; i < n; i++) {
        string word;
        cin >> word;
        count[word]++;
    }
    vector<pair<int, string>> ranking;
    for (auto entry : count) {
        ranking.push_back({-entry.second, entry.first});
    }
    sort(ranking.begin(), ranking.end());
    int shown = min(m, (int)ranking.size());
    for (int i = 0; i < shown; i++) {
        cout << ranking[i].second << ' ' << -ranking[i].first << '\n';
    }
    return 0;
}
