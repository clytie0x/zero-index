#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    vector<int> arrive(n), pages_left(n);
    for (int i = 0; i < n; i++) {
        cin >> arrive[i] >> pages_left[i];
    }
    vector<long long> finish(n);
    queue<int> waiting;
    long long now = 0;
    int next = 0;
    int done = 0;
    while (done < n) {
        if (waiting.empty()) {
            now = max(now, (long long)arrive[next]);
        }
        while (next < n && arrive[next] <= now) {
            waiting.push(next);
            next++;
        }
        int job = waiting.front();
        waiting.pop();
        int printed = min(pages_left[job], k);
        now += printed;
        pages_left[job] -= printed;
        while (next < n && arrive[next] <= now) {
            waiting.push(next);
            next++;
        }
        if (pages_left[job] > 0) {
            waiting.push(job);
        } else {
            finish[job] = now;
            done++;
        }
    }
    for (int i = 0; i < n; i++) {
        cout << finish[i] << '\n';
    }
    return 0;
}
