#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    map<int, int> votes;
    for (int i = 0; i < n; i++) {
        int song;
        cin >> song;
        votes[song]++;
    }
    int best_song = 0;
    int best_votes = 0;
    for (auto entry : votes) {
        if (entry.second > best_votes) {
            best_song = entry.first;
            best_votes = entry.second;
        }
    }
    cout << best_song << ' ' << best_votes << '\n';
    return 0;
}
