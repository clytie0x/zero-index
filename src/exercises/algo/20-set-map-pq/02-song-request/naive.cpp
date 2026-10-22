#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> songs;
    vector<int> votes;
    for (int i = 0; i < n; i++) {
        int song;
        cin >> song;
        bool found = false;
        for (int j = 0; j < (int)songs.size(); j++) {
            if (songs[j] == song) {
                votes[j]++;
                found = true;
                break;
            }
        }
        if (!found) {
            songs.push_back(song);
            votes.push_back(1);
        }
    }
    int best = 0;
    for (int j = 1; j < (int)songs.size(); j++) {
        if (votes[j] > votes[best] || (votes[j] == votes[best] && songs[j] < songs[best])) {
            best = j;
        }
    }
    cout << songs[best] << ' ' << votes[best] << '\n';
    return 0;
}
